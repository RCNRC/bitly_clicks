# bitly_clicks

Это python скрипт. При запуске попросит ввести ссылку. При вводе обычной ссылки скрипт создаёт укороченную ссылку формата https://bit.ly/abcde и возвращает её id. При вводе укороченной ссылки выводит число переходов по ссылке.

Работает с сайтом https://bitly.com

## Установка

Скачать гит репозиторий. В корне репозитория создать файл `.env` и поместить внутрь строку `ACCESS_TOKEN=ваш токен`, где заменить строку `ваш токен` на ваш уникальный токен.

## Требования к использованию

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:


1. Для Unix/macOs: `python -m pip install -r ~/bitly_clicks/requirements.txt`
2. Для Windows: `py -m pip download --destination-directory DIR -r requirements.txt`

## Использование

Запустить файл bitly.py как Python скрипт.

## Пример использования

Запуск:
```cmd
python3 ~bitly_clicks/bitly.py
```

Вывод:
```cmd
Введите ссылку: https://github.com/
Битлинк: bit.ly/...
```