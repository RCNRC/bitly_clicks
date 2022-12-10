from urllib.parse import urlparse
from dotenv import dotenv_values
import requests
import argparse


def shorten_bitlink(url, token):
    api_endpoint = f"https://api-ssl.bitly.com/v4/shorten"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"long_url": url}
    response = requests.post(api_endpoint, headers=headers, json=body)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(url, token):
    parsed_url = urlparse(url)
    api_endpoint = (
        f"https://api-ssl.bitly.com/v4/bitlinks/"
        f"{parsed_url.netloc}{parsed_url.path}/clicks/summary"
    )
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url, token):
    parsed_url = urlparse(url)
    api_endpoint = (
        f"https://api-ssl.bitly.com/v4/bitlinks/"
        f"{parsed_url.netloc}{parsed_url.path}"
    )
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_endpoint, headers=headers)
    return response.ok


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', nargs='?')
    return parser.parse_args()


def main():
    token = dotenv_values(".env")["BITLY_API_ACCESS_TOKEN"]
    arguments = get_arguments()
    user_url = arguments.link if arguments.link else input("Введите ссылку: ")
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
