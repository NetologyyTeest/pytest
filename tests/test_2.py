import unittest
import requests
from task_2 import folder
from token_1 import TOKEN


class YandexTest(unittest.TestCase):  # Тест на успешное создание папки

    URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    params = {'path': folder}
    response = requests.get(f'{URL}', headers=headers, params=params)
    result = response.status_code

    def test_successful_response(self):
        self.assertEqual(self.result, 200)

    def test_error_response(self):
        self.assertNotEqual(self.result, 404)


if __name__ == '__main__':
    unittest.main()