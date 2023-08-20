from work_with_file import write_new_data, read_all
from utils import paginating


def main():
    user_choice: str = input('введите 1 если хотите добавить или 2 для просмотра ')

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
        data: list = read_all()

        # можно установить любой размер страницы больше 1
        page_size: int = 2
        total_page: int = round(len(data) / page_size)
        print(f'всего страниц  {total_page}')

        paginating(data, page_size, total_page)


if __name__ == "__main__":
    main()
