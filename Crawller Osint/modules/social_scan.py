import requests
import concurrent.futures

SOCIAL_PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Medium": "https://medium.com/@{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "About.me": "https://about.me/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Telegram": "https://t.me/{}",
    "WordPress": "https://{}.wordpress.com",
    "Ask.fm": "https://ask.fm/{}",
    "Flipboard": "https://flipboard.com/@{}",
    "VKontakte": "https://vk.com/{}",
    "OK.ru": "https://ok.ru/{}"
}

headers = {'User-Agent': 'Mozilla/5.0'}

def check_single(platform, url, username):
    profile_url = url.format(username)
    try:
        response = requests.get(profile_url, headers=headers, timeout=5)
        if response.status_code == 200:
            return (platform, profile_url)
    except:
        pass
    return (platform, None)

def check_username(username):
    results = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        futures = []
        for platform, url in SOCIAL_PLATFORMS.items():
            futures.append(executor.submit(check_single, platform, url, username))

        for future in concurrent.futures.as_completed(futures):
            platform, link = future.result()
            results[platform] = link

    return results

