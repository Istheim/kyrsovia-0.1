from abc import ABC

import requests
from fetch_data_api import ApiConnector
from pprint import pprint


class SuperJobApi(ApiConnector, ABC):
    """Класс для подключения к API superjob.ru"""
    def __init__(self):
        self.api_url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {"Host": "api.superjob.ru",
                        "X-Api-App-Id": "v3.h.4487627.79a3e9c97503c38b8bfd1d487c9f75fe744075df.b95c558db32b3efe586d69ce950d787d6048b84f",
                        "Authorization": "Bearer r.000000010000001.example.access_token",
                        "Content-Type": "application/x-www-form-urlencoded"
                        }

    def fetch_data(self):
        """Метод для получения вакансий"""
        return requests.get(self.api_url, headers=self.headers).json()


s = SuperJobApi()
pprint(s.fetch_data())
