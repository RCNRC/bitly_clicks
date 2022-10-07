from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import requests
load_dotenv()

URL_BITLY = "https://api-ssl.bitly.com/v4/"


def post_shorten_bitlink(url, token=os.environ["ACCESS_TOKEN"]):
    page = "shorten"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"long_url": url}
    response = requests.post(f"{URL_BITLY}{page}", headers=headers, json=body)
    response.raise_for_status()
    return response.json()["id"]


def get_bitlink_clicks_count(bit_url, token=os.environ["ACCESS_TOKEN"]):
    parsed = urlparse(bit_url)
    page = f"bitlinks/{parsed.netloc}{parsed.path}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{URL_BITLY}{page}", headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url):
    parsed = urlparse(url)
    return parsed.netloc=="bit.ly"


def main():
    user_url = input("Введите ссылку: ")
    if(is_bitlink(user_url)):
        try:
            print(f"По вашей ссылке прошли: {get_bitlink_clicks_count(bit_url=user_url)}")
        except requests.exceptions.HTTPError:
            print("Ошибка: не удалось получить число кликов.")
            return
    else:
        try:
            print(f"Битлинк: {post_shorten_bitlink(url=user_url)}")
        except requests.exceptions.HTTPError:
            print("Ошибка: битлинк не был создан.")
            return


if __name__ == '__main__':
    main()
