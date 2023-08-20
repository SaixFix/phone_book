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
