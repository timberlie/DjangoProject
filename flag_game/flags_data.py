# Данные о флагах: файл -> название страны
FLAGS_DATABASE = {
    1: {"file": "1.png", "country": "Россия"},
    2: {"file": "2.png", "country": "США"},
    3: {"file": "3.png", "country": "Франция"},
    4: {"file": "4.png", "country": "Германия"},
    5: {"file": "5.png", "country": "Италия"},
    6: {"file": "6.png", "country": "Испания"},
    7: {"file": "7.png", "country": "Великобритания"},
    8: {"file": "8.png", "country": "Япония"},
    9: {"file": "9.png", "country": "Китай"},
    # 10: {"file": "10.png", "country": "Индия"},
    # 11: {"file": "11.png", "country": "Бразилия"},
    # 12: {"file": "12.png", "country": "Канада"},
    # 13: {"file": "13.png", "country": "Австралия"},
    # 14: {"file": "14.png", "country": "Мексика"},
    # 15: {"file": "15.png", "country": "Турция"},
    # 16: {"file": "16.png", "country": "Нидерланды"},
    # 17: {"file": "17.png", "country": "Швеция"},
    # 18: {"file": "18.png", "country": "Норвегия"},
    # 19: {"file": "19.png", "country": "Финляндия"},
    # 20: {"file": "20.png", "country": "Польша"},
}

# Получить случайные 3 разных флага
import random

def get_random_flags(exclude_id=None):
    all_ids = list(FLAGS_DATABASE.keys())
    if exclude_id:
        all_ids = [i for i in all_ids if i != exclude_id]
    return random.sample(all_ids, min(3, len(all_ids)))

# Получить данные флага по ID
def get_flag_by_id(flag_id):
    return FLAGS_DATABASE.get(flag_id)

# Получить страну по ID
def get_country_by_id(flag_id):
    flag = FLAGS_DATABASE.get(flag_id)
    return flag["country"] if flag else None