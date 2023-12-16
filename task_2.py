import requests
from token_1 import TOKEN

URL='https://cloud-api.yandex.net/v1/disk/resources/'
headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
folder = 'Python_test'

def create_folder():
    """Создание папки"""
    params = {'path': folder}
    res = requests.put(f'{URL}', headers=headers, params=params)
    return res.status_code

def check_folder():
    """Проверяем наличие папки"""
    params = {'path': folder}
    res = requests.get(f'{URL}', headers=headers, params=params)
    return res.status_code


if __name__ == '__main__':
    print(create_folder())
