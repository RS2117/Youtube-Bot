from pytube import YouTube
import os

# Read YouTube links from a text file
with open('links.txt', 'r') as file:
    links = file.read().splitlines()

# Specify the directory where you want to save the downloaded videos
download_dir = './downloads/'

# Create the downloads directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Loop through each YouTube link and download the video
for index, link in enumerate(links, start=1):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        video_title = f'vid{index}.mp4'
        print(f"Downloading: {video_title}")
        stream.download(output_path=download_dir, filename=video_title)
        print(f"Downloaded: {video_title}")
    except Exception as e:
        print(f"Error downloading {link}: {str(e)}")

print("All downloads completed!")
