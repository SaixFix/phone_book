from work_with_file import write_new_data, read_all
from utils import paginating, search_one


def main():
    # вся информация из справочника
    all_data: list = read_all()

    user_choice: str = input(
        'введите:\n 1 если хотите добавить,\n 2 для просмотра всего справочника,\n'
        ' 3 Поиск записей по одной или нескольким характеристикам\n '
    )

    if user_choice == '1':
        # шаблон словаря
        data: dict = {
            'Фамилия': '',
            'Имя': '',
            'Отчество': '',
            'название компании': '',
            'рабочий телефон': '',
            'телефон личный (сотовый)': ''
        }

        # Записываем в словарь новые данные от юзера
        for row in data:
            data[row]: str = input(f'{row} ')

        write_new_data(data)

    if user_choice == '2':
        # можно установить любой размер страницы больше 1
        page_size: int = 2
        total_page: int = round(len(all_data) / page_size)
        print(f'всего страниц  {total_page}')

        paginating(all_data, page_size, total_page)

    if user_choice == '3':
        search_one(all_data)


if __name__ == "__main__":
    main()
