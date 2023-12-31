import json


def converter_to_str(dict_data: dict) -> str:
    """
    Функция принимает словарь, перебирает его
     по паре ключ, значение и добавляет переносы строки
    """
    str_data = '\n'
    for k, v in dict_data.items():
        str_data += f"{''.join(k)}: {''.join(v)}, \n"
    return str_data


def paginating(data: list[dict], page_size: int, total_page: int) -> None:
    """
    Функция разбивки базы на страницы
     и вывода требуемой через print
    """

    # цикл показывает требуемую страницу либо break по команде или при несуществующей странице
    while True:
        user_input: str = input(
            'введите номер страницы либо слово "выход" чтобы выйти из просмотра '
        )
        # проверяем, если не число то либо выход, либо цикл заново
        if not user_input.isdigit():
            if user_input == 'выход':
                break
            continue

        # переводим запрошеную страницу в число
        requested_page: int = int(user_input)
        # формула для страниц после 3 включительно
        page_after_3: int = (requested_page * page_size) - page_size

        # показываем страницы в зависимости от запрошенных
        if requested_page == 1:
            # применяем функцию десериализации словарей к каждому из требуемого страничного среза
            page = list(map(converter_to_str, data[0:page_size]))
            # выводим список в виде строки
            print(''.join(page))
        if requested_page == 2:
            page = list(map(converter_to_str, data[page_size:requested_page * page_size]))
            print(''.join(page))
        if requested_page >= 3:
            page = list(map(converter_to_str, data[page_after_3:(page_after_3 + page_size)]))
            print(''.join(page))

        # если требуемая страница за рамками существующих
        if requested_page > total_page:
            print('Конец справочника')


def search(data: list[dict]) -> list[dict]:
    """
    Функция поиска по одному или нескольким параметрам.
    Получает базу(список словарей), возвращает результат поиска
    """

    user_choice = (input('Введите искомые параметры через запятую\n')).lower()
    # удаляем пробелы в начале и конце
    user_choice = user_choice.strip()
    # удаляем пробелы после запятой
    user_choice = user_choice.replace(', ', ',')
    # удаляем пробелы перед запятой
    user_choice = user_choice.replace(' ,', ',')
    # Создаем список ключевых слов из запроса пользователя деля по запятой
    search_data = user_choice.split(',')
    result = []

    # цикл в котором мы сравниваем значения каждого абонента
    # в нижнем регистре со списком ключевых слов
    # и при полном совпадении добавляем его в result
    for row in data:
        count_match = 0
        for value in search_data:
            if value in [x.lower() for x in row.values()]:
                count_match += 1
        if count_match == len(search_data):
            result.append(row)

    # Выводим результат
    if len(result) == 0:
        print('Абонента с такими параметрами нет')

    # применяем функцию десериализации словарей
    output = list(map(converter_to_str, result))
    # выводим список в виде строки
    print(''.join(output))

    return result


def redact_one(template: dict, result_search: list[dict]) -> None:
    """
    Функция для редактирования 1ой записи и затем замены ее в общей базе.
    Получает шаблон записи, запись для редактирования.
    """

    # Выбираем требуемый ключ
    key_choice = int(input(
        f'Введите номер параметра для редактирования\n'
        f'{json.dumps(template, ensure_ascii=False, indent=4)}\n'
    ))

    # Вводим новое значение
    new_value = input('Введите новое значение\n')
    # Переписываем старое значение на новое по выбранному ключу
    result_search[0][list(template.keys())[key_choice]] = new_value

    # применяем функцию десериализации словарей
    output = list(map(converter_to_str, result_search))
    # выводим список в виде строки
    print(
        f'Данные изменены'
        f'{"".join(output)}'
    )
