import requests
from fetch_data_api import ApiConnector
from pprint import pprint


class HhConnectApi(ApiConnector):
    """Класс для подключения к API hh.ru"""

    def __init__(self):
        self.api_url = 'https://api.hh.ru/vacancies/'

    def fetch_data(self):
        """Метод для получения вакансий"""
        return requests.get(self.api_url).json()


h = HhConnectApi()
pprint(h.fetch_data())


