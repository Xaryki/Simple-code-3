import json

"""Сбросить JSON"""

def create_json():
    return {"chat_id": {"xls_url": "...",
                        "group_number": 2101, "menu_stage": "...", "bot_message_id": 31
                        }
            }


dictionary = create_json()

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(dictionary, file, ensure_ascii=False, indent=4)
    file.write('\n')

