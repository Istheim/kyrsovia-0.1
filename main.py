from vacancy import Vacancy
import json
from builtins import *


def process_user_input():
    job = []  # Создаем пустой список для хранения экземпляров класса "Vacancy"

    try:
        # Открывает файл "list.json" в режиме чтения
        with open("list.json", "r", encoding='utf-8') as f:
            # Загружает данные из файла в переменную "vacancies"
            vacancies = json.load(f)

            # Достаем значения из файла json для платформы hh.ru
            for vacancy_data in vacancies[0]['items']:
                title = vacancy_data['name']
                if 'salary' in vacancy_data and vacancy_data['salary'] is not None:
                    if 'from' in vacancy_data['salary']:
                        salary_min = vacancy_data['salary']['from']
                    else:
                        salary_min = None
                    if 'to' in vacancy_data['salary']:
                        salary_max = vacancy_data['salary']['to']
                    else:
                        salary_max = None
                else:
                    salary_min = None
                    salary_max = None
                url = vacancy_data['area']['url']
                requirement = vacancy_data['snippet']['requirement']
                # Создаем экземпляр класса Vacancy
                vacancy_hh = Vacancy(title, salary_min, salary_max, url, requirement)
                # Добавляем экземпляры в список job
                job.append(vacancy_hh)

            # Достаем значения из файла json для платформы superjob.ru
            for vacancy_data in vacancies[1]['objects']:
                title = vacancy_data['profession']
                salary_min = vacancy_data['payment_from']
                salary_max = vacancy_data['payment_to']
                url = vacancy_data['client']['link']
                requirement = vacancy_data['candidat']
                # Создаем экземпляр класса Vacancy
                vacancy_s = Vacancy(title, salary_min, salary_max, url, requirement)
                # Добавляем экземпляры в список job
                job.append(vacancy_s)

    except FileNotFoundError:
        print("File not found")
    except KeyError:
        print("No key")

    while True:
        user_input = input("Введите поисковый запрос: ")
        # Флаг для отслеживания, найдена ли вакансия
        found = False

        for vacancy_all in job:
            if user_input == vacancy_all.title:
                print(vacancy_all)
                # Установка флага в True, если найдена вакансия
                found = True

        if not found:
            print(f"Нет вакансий, соответствующих заданным критериям.")

        continue_search = input("Продолжить поиск? (да/нет): ")
        if continue_search.lower() != "да":
            break


if __name__ == "__main__":
    process_user_input()

