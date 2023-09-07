import requests

url = "https://www.imdb.com/"
headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.imdb.com/",
    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()  # Raise an exception if the response is not successful

    with open(file="IMDB.html", mode="wt", encoding="utf-8") as files:
        files.write(response.text)
        print("Successfully saved HTML content to IMDB.html")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except IOError as e:
    print(f"File error: {e}")
