import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Log in to an Instagram account (optional, required only for private accounts)
login_successful = L.login("kiddomiddy@gmail.com", "Hittheblack21")

if login_successful:
    # Download a specific Instagram Reel
    reel_url = 'https://www.instagram.com/reel/CylifK2RUiE/'
    L.download_videos([reel_url])

    # Download multiple Reels by providing a list of URLs
    # reel_urls = ['url1', 'url2', 'url3']
    # L.download_reels(reel_urls)
else:
    print("Login failed. Make sure your login credentials are correct.")
