import json


class JSON_methods:
    """Методы с JSON"""

    @classmethod
    def create_user(cls,person: dict):
        """Создания словаря без chat_id"""
        return {"xls_url": person["xls_url"],
                "group_number": person["group_number"], "menu_stage": person["menu_stage"],
                "bot_message_id": person["bot_message_id"]
                }

    @classmethod
    def json_to_dict(cls):
        """Преобразование JSON в Dictionary"""
        with open('data.json', 'r', encoding='utf-8') as file:
            dictionary = json.load(file)
        return dictionary

    @classmethod
    def dict_to_json(cls,dictionary_json):
        """Преобразование Dictionary в JSON"""
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(dictionary_json, file, ensure_ascii=False, indent=4)

    @classmethod
    def add_new_user_to_json(cls,dictionary: dict, user: dict, person: dict):
        """Добавление пользователя в общий словарь"""
        dictionary[person["chat_id"]] = user


"""user - это словарь с данными о пользователе без chat_id и должен создаваться из create_user
   person - это собранные даныне о пользователе
"""