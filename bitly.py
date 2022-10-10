from urllib.parse import urlparse
from dotenv import dotenv_values
import requests

DOMAIN = "api-ssl.bitly.com/"
PROTOCOL = "https://"


def shorten_bitlink(url, token):
    path = "v4/shorten"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"long_url": url}
    response = requests.post(f"{PROTOCOL}{DOMAIN}{path}", headers=headers, json=body)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(url, token):
    parsed_url = urlparse(url)
    path = f"v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{PROTOCOL}{DOMAIN}{path}", headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url, token):
    parsed_url = urlparse(url)
    path = f"v4/bitlinks/{parsed_url.netloc}{parsed_url.path}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{PROTOCOL}{DOMAIN}{path}", headers=headers)
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
