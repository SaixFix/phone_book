from class_person import Person
from work_with_file import read_all, rewrite_data
from utils import paginating, search, redact_one
from dataclasses import asdict


def main():
    # вся информация из справочника
    all_data: list[dict] = read_all()

    # шаблон
    data: dict = {
        'Фамилия': '0',
        'Имя': '1',
        'Отчество': '2',
        'название компании': '3',
        'рабочий телефон': '4',
        'телефон личный (сотовый)': '5'
    }

    exit_func = False  # переменная для выхода из цикла

    while not exit_func:
        user_choice: str = input(
            'введите:\n 1 если хотите добавить,\n 2 для просмотра всего справочника,\n'
            ' 3 Поиск записей по одной или нескольким характеристикам и редактирование\n'
            ' 4 для выхода из программы\n'
        )
        if user_choice == '4':
            exit_func = True
        if user_choice == '1':

            # Записываем в словарь новые данные от юзера
            for row in data:
                data[row]: str = input(f'{row} ')

            all_data.append(data)
            rewrite_data(all_data)
            continue

        if user_choice == '2':
            # можно установить размер страницы больше 1
            page_size: int = 2
            total_page: int = round(len(all_data) / page_size)
            print(f'всего страниц  {total_page}')

            paginating(all_data, page_size, total_page)

        if user_choice == '3':
            result_search = search(all_data)
            step_2 = input('Желаете отредактировать найденный результат, введите да или нет\n').lower()
            if step_2 == 'да':
                if len(result_search) > 1:
                    print('Найдено больше 1 результата попробуйте заново, уточните данные дня поиска')
                if len(result_search) == 1:
                    redact_one(data, result_search)
                    rewrite_data(all_data)
                    continue


if __name__ == "__main__":
    main()
