import json
from builtins import *
from abc import ABC, abstractmethod
from vacancy import Vacancy


class AbstractDataSaver(ABC):
    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def search_vacancy(self, title):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy):
        pass


class LocalDataSaver(AbstractDataSaver):
    """Класс локального хранения, отвечающий за сохранение, загрузку и работу с данными о вакансиях локально."""

    def __init__(self, path):
        self.__path = path

    def save_data(self, data):
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(data, f, sort_keys=False, indent=2, ensure_ascii=False)

    def load_data(self):
        with open(self.__path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def search_vacancy(self, title):
        data = self.load_data()
        found_vacancies = []
        for vacancy_data in data:
            if vacancy_data['title'] == title:
                vacancy = Vacancy(vacancy_data['title'], vacancy_data['url'], vacancy_data['salary_min'],
                                  vacancy_data['salary_max'], vacancy_data['requirement'])
                found_vacancies.append(vacancy)
        return found_vacancies

    def add_vacancy(self, vacancy):
        data = self.load_data()
        data.append(vacancy.as_dict())
        self.save_data(data)

    def remove_vacancy(self, vacancy):
        data = self.load_data()
        data = [v for v in data if v['url'] != vacancy.url]
        self.save_data(data)


saver = LocalDataSaver("list.json")