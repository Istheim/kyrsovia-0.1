from abc import ABC, abstractmethod
from builtins import *


class ApiConnector(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def fetch_data(self):
        print('Get api')
