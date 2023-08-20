import json


def read_all() -> list:
    """
    Читаем из файла справочника
    """
    with open('./telbook.json', 'r', encoding='utf-8') as file:
        data: list = json.load(file)
        return data


def write_new_data(data: dict) -> None:
    """
    Добавляем новую строчку в файл справочника
    """
    with open('./telbook.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return print('Абонент добавлен', data)
