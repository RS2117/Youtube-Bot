import time
import os
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




# Define a function to set up the WebDriver with custom options and service
def setup_driver():
    service = Service(executable_path='./chromedriver.exe')

    options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--log-level=3")
    options.add_argument("user-data-dir=C:\\Users\\rajan\\AppData\\Local\\Google\\Chrome for Testing\\User Data\\")
    options.binary_location = "C:\\Users\\rajan\\Desktop\\New folder\\chrome\\chrome.exe"

    # Initialize the Chrome WebDriver with the configured service and options
    return webdriver.Chrome(service=service, options=options)

# Define a function to modify links in an input file and save them to an output file
def modify_links(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if line.startswith("https://www.youtube.com/watch?v="):
            video_id = line.split("v=")[1].strip()
            new_url = f"https://youtubetranscript.com/?v={video_id}\n"
            new_lines.append(new_url)
        else:
            new_lines.append(line)

    with open(output_file, 'w') as file:
        file.writelines(new_lines)

    print("Links have been modified and saved to 'Modified_Ylinks.txt'")

# Define a function to open URLs, click the button, and save the transcript
def open_and_click_button(driver, url, script_file_dir, chat_message):
    driver.get(url.strip())

    # Wait for 5 seconds (you can adjust the time as needed)
    time.sleep(10)

    try:
        # Find the button with the text "Copy entire transcript" and click it
        button = driver.find_element(By.XPATH, '//button[contains(text(), "Copy entire transcript")]')
        button.click()
        print('Button clicked')
    except:
        print('Button not found or unable to click.')

   
    driver.get("https://chat.openai.com/")

    time.sleep(10)

    textarea = driver.find_element(By.ID, 'prompt-textarea')
    textarea.clear()
    textarea.send_keys(Keys.CONTROL, 'v')
    textarea.send_keys(chat_message)

    time.sleep(3)

    # Find and click the first button
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/form/div/div[2]/div/button')
    button.click()
    print('Button clicked GPT')

    time.sleep(120)  

    button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/button')
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()
    print('Button clicked Copy')

     # Get the transcript from the clipboard
    transcript = pyperclip.paste()

    # Clear the contents of the file
    with open(script_file_dir, 'w') as script_file:
        pass
    
    # Write the transcript to a new text document under a title
    with open(script_file_dir, 'a') as script_file:
        script_file.write(transcript)
        script_file.write("\n\n")

    print(f"Transcript saved to '{script_file_dir}'")

def go_to_pictory_ai(driver, script_file):
    driver.get("https://app.pictory.ai/textinput")

    # Wait for the page to load (you can adjust the time as needed)
    time.sleep(10)

    # Find the button by its class name
    #button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/div/div/div[3]/button')
    element = driver.find_element(By.XPATH, '//button[contains(text(), "Proceed")]')
   
    # Click the button
    element.click()

    time.sleep(10)

    element = driver.find_element(By.CSS_SELECTOR, 'div.ck-content[contenteditable="true"]')
    element.click()
    
    # Read the script content from the script file
    with open(script_file, 'r') as script_file:
        script_content = script_file.read()
        pyperclip.copy(script_content)
    
    # Paste the script content into the Pictory.ai textarea
    element.send_keys(Keys.CONTROL, 'v')

    time.sleep(20)

    element = driver.find_element(By.XPATH, '//button[contains(text(), "Proceed")]')
    element.click()

    time.sleep(60)

    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/div/button[2]')
    element.click()

    time.sleep(10)

    element = driver.find_element(By.XPATH, '//html/body/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]')
    element.click()

    time.sleep(1)
    
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[1]')
    element.click()

    time.sleep(180)

    # image_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]/div/div[55]/div/div[1]')
    # # Click on the image
    # image_element.click()
    # time.sleep(2)

    # time.sleep(2)

    # svg_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]/div/div[55]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]')
    # svg_element.click()

    # time.sleep(120)

    #audio
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/nav/ul/li[3]')
    element.click()

    #fav
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/main/section/div/div[1]/div/div[3]/div/ul/li[5]')
    element.click()

    #selecting voice
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/main/section/div/div[1]/div/div[3]/div/div/div[5]/div/div/div/div/div[2]/div[2]/div/ol/li/a/div')
    # Create an ActionChains object
    actions = ActionChains(driver)
    # Hover over the element
    actions.move_to_element(element).perform()

    #selecting voice
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/main/section/div/div[1]/div/div[3]/div/div/div[5]/div/div/div/div/div[2]/div[2]/div/ol/li/a/div/div[2]/div/div')
    element.click()

    time.sleep(2)

    # #select style
    # element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/nav/ul/li[6]')
    # element.click()

    # time.sleep(1)

    # #select mY-style
    # element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/main/section/div/div[1]/div/div[4]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/button[2]')
    # element.click()
    
    # time.sleep(1)

    # #select style
    # element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/main/section/div/div[1]/div/div[5]/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]')
    # element.click()
    
    #Hovering download
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/main/header/div/div/div/div[2]/div[3]/a')
    # Create an ActionChains object
    actions = ActionChains(driver)
    # Hover over the element
    actions.move_to_element(element).perform()

    time.sleep(2)

    #download video
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div[7]/main/header/div/div/div/div[2]/div[3]/div/a[1]')
    element.click()

    time.sleep(300)

    #download video
    element = driver.find_element(By.XPATH, '/html/body/div[9]/div[3]/div/div[3]/div[2]/button')
    element.click()

    time.sleep(240)




# Set up the WebDriver
driver = setup_driver()

# Define the path to the directory where your transcript files are located
transcript_directory = "Transcripts"

# Get a list of all transcript files in the directory
transcript_files = os.listdir(transcript_directory)

# Define the chat message you want to send
chat_message = " make a YouTube video script out of above transcript without highlights [such as narrator, onscreen, offscreen , host , etc]"


# Define the path to the input file
input_file = "Ylinks.txt"

# Define the path to the output file for modified links
output_file_modified = "Modified_Ylinks.txt"

# Modify the links in the input file and save them to the output file
modify_links(input_file, output_file_modified)

# Define the path to the output file for transcripts
output_directory = "Transcripts"  # Create a directory to store transcripts

# Create the transcripts directory if it doesn't exist
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# Read the contents of the modified input file and open each modified link
with open(output_file_modified, 'r') as file:
    lines = file.readlines()

for index, line in enumerate(lines):
   output_file_transcript = os.path.join(output_directory, f"script{index + 1}.txt")
   open_and_click_button(driver, line, output_file_transcript, chat_message)

# Iterate through the transcript files and process them on Pictory.ai
for transcript_file in transcript_files:
    transcript_file_path = os.path.join(transcript_directory, transcript_file)
    go_to_pictory_ai(driver, transcript_file_path)


# Close the WebDriver when you're done
driver.quit()
