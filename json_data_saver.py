import json
from builtins import *
from hhru_api import HhConnectApi
from superjobru_api import SuperJobApi


class JSONDataSaver(HhConnectApi, SuperJobApi):
    """Сохраняем все вакансии в json файл"""

    def save_json(self):
        hh_api = HhConnectApi()
        s_api = SuperJobApi()
        all_api = [hh_api.fetch_data(), s_api.fetch_data()]

        with open("list.json", "w", encoding="utf-8") as f:
            json.dump(all_api, f, sort_keys=False, indent=2, ensure_ascii=False)


saver = JSONDataSaver()
saver.save_json()
