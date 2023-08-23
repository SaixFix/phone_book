import json


def read_all() -> list[dict]:
    """
    Читаем из файла справочника,
    Возвращаем список словарей
    """
    with open('./telbook.json', 'r', encoding='utf-8') as file:
        data: list[dict] = json.load(file)
        return data


def add_new_data(data: dict) -> None:
    """
    Получаем словарь,
    Добавляем новую строчку в файл справочника
    """
    with open('./telbook.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return print('Абонент добавлен', data)


def rewrite_data(new_all_data: list[dict]) -> None:
    """
    Перезаписываем файл.
    Получаем список словарей - база с обновленными данными
    """
    with open('./telbook.json', 'w', encoding='utf-8') as file:
        json.dump(new_all_data, file, ensure_ascii=False, indent=4)
    return print('Информация базы обновлена')


