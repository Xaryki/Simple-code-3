import json
from random import randint


def create_user(person: dict):
    """Создания словаря без chat_id"""
    return {"xls_url": person["xls_url"],
            "group_number": person["group_number"], "menu_stage": person["menu_stage"],
            "bot_message_id": person["bot_message_id"]
            }


def create_user2(xls_url: str, group_number: int, menu_stage: str, bot_message_id: int):
    """Создания словаря без chat_id"""
    return {"xls_url": xls_url,
            "group_number": group_number, "menu_stage": menu_stage,
            "bot_message_id": bot_message_id
            }


def json_to_dict():
    """Преобразование JSON в Dictionary"""
    with open('data.json', 'r', encoding='utf-8') as file:
        dictionary = json.load(file)
    return dictionary


def dict_to_json(dictionary_json):
    """Преобразование Dictionary в JSON"""
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(dictionary_json, file, ensure_ascii=False, indent=4)


"""dictionary - словарь с пользователями
   person - данные об пользователе
"""
person = {"chat_id": 134314}

# person = {"chat_id": 34113, "xls_url": "yandex.com", "group_number": 2101, "menu_stage": "xz", # данные о пользователе
#          "bot_message_id": 2343}
user = create_user2("fd", 42342, "fdsfds", 344)  # Создание нормального словаря
dictionary = json_to_dict()  # JSON --> dict


def add_new_user_to_json(dictionary: dict, user: dict):
    dictionary[person["chat_id"]] = user  # create abd add user to dict

    dict_to_json(dictionary)  # dict --> json


"""Один пользователь в таблицу"""
add_new_user_to_json(dictionary, user)

"""Рандомный забив JSON
for i in range(1, randint(10, 50)):
    person = {"chat_id": randint(100, 1000), "xls_url": "yandex.com", "group_number": randint(1000, 3000),
              "menu_stage": "xz", "bot_message_id": randint(100, 1000)}
    add_new_user_to_json(person)
"""
