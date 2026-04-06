"""Данные о флагах для игры "Угадай флаги"."""

import random

# Данные о флагах: ID -> файл и название страны
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
}


def get_random_flags(exclude_id=None):
    """
    Возвращает список из 3 случайных ID флагов.

    Args:
        exclude_id: ID флага, который нужно исключить из выборки.

    Returns:
        list: Список из 3 случайных ID флагов.
    """
    all_ids = list(FLAGS_DATABASE.keys())
    if exclude_id:
        all_ids = [i for i in all_ids if i != exclude_id]
    return random.sample(all_ids, min(3, len(all_ids)))


def get_flag_by_id(flag_id):
    """
    Возвращает данные флага по его ID.

    Args:
        flag_id: ID флага.

    Returns:
        dict: Словарь с данными флага или None, если флаг не найден.
    """
    return FLAGS_DATABASE.get(flag_id)


def get_country_by_id(flag_id):
    """
    Возвращает название страны по ID флага.

    Args:
        flag_id: ID флага.

    Returns:
        str: Название страны или None, если флаг не найден.
    """
    flag = FLAGS_DATABASE.get(flag_id)
    return flag["country"] if flag else None