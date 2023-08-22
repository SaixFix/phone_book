import json


def paginating(data: list, page_size: int, total_page: int) -> None:
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
            print(data[0:page_size])
        if requested_page == 2:
            print(data[page_size:requested_page * page_size])
        if requested_page >= 3:
            print(data[page_after_3:(page_after_3 + page_size)])

        # если требуемая страница за рамками существующих
        if requested_page > total_page:
            print('Конец справочника')


def search_one(data: list) -> None:
    """Функция поиска по одному или нескольким параметрам"""

    user_choice = (input('Введите искомые параметры через запятую')).lower()
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
    # json.dumps для более красивого вывода
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=4))
