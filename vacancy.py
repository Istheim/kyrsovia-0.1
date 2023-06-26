import json
from json_data_saver import JSONDataSaver
from pprint import pprint


class Vacancy:
    def __init__(self, title, url, salary_min, salary_max, requirement):
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.requirement = requirement

    def __str__(self):
        return f"{self.title}, {self.url}, {self.salary_min}, {self.salary_max}, {self.requirement}"