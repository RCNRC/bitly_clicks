from urllib.parse import urlparse
import os
from dotenv import dotenv_values
import requests

URL_BITLY = "https://api-ssl.bitly.com/v4/"


def shorten_bitlink(url, token):
    endpoint_api = "shorten"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"long_url": url}
    response = requests.post(f"{URL_BITLY}{endpoint_api}", headers=headers, json=body)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(url, token):
    url_parsed = urlparse(url)
    endpoint_api = f"bitlinks/{url_parsed.netloc}{url_parsed.path}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{URL_BITLY}{endpoint_api}", headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url, token):
    url_parsed = urlparse(url)
    endpoint_api = f"bitlinks/{url_parsed.netloc}{url_parsed.path}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{URL_BITLY}{endpoint_api}", headers=headers)
    return response.ok


def main():
    token = dotenv_values(".env")["BITLY_API_ACCESS_TOKEN"]
    user_url = input("Введите ссылку: ")
    if is_bitlink(user_url, token):
        try:
            print(f"По вашей ссылке прошли: {count_clicks(user_url, token)} раз(а)")
        except requests.exceptions.HTTPError:
            print("Ошибка: не удалось получить число кликов.")
    else:
        try:
            print(f"Битлинк: {shorten_bitlink(user_url, token)}")
        except requests.exceptions.HTTPError:
            print("Ошибка: битлинк не был создан.")


if __name__ == '__main__':
    main()
