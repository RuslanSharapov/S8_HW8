#    Дополнить телефонный справочник возможностью изменения и удаления данных.
#    Пользователь также может ввести имя или фамилию,  
#    и Вы должны реализовать функционал для изменения и удаления данных.



# функция добавления новой записи в телефонную книгу
def add_data():
    with open(filename, 'a', encoding='utf-8') as f:
        surname = input('Введите Фамилию: ')
        name = input('Введите Имя: ')
        patronymic = input('Введите Отчество: ')
        phone = input('Введите номер телефона: ')
        f.write(f'{surname}, {name}, {patronymic}, {phone}\n')
    print('Запись успешно добавлена')

# функция отображения всех записей в телефонной книге
def display_data():
    with open(filename, 'r', encoding='utf-8') as f:
        print('Записи в телефонной книге:')
        for line in f:
            surname, name, patronymic, phone = line.strip().split(',')
            print(f'{surname}, {name}, {patronymic}, {phone}')

# функция поиска элементов
def search_data():
    with open(filename, 'r', encoding='utf-8') as f:
        text = input('Введите текст для поиска: ')
        for line in f:
            if text in line:
                print(line.strip())
            else:
                print('Данный контакт не найден')

# функция экспорта данных
def export_data():
    with open(filename, 'r', encoding='utf-8') as f:
        with open('phonebook_export.txt', 'w', encoding='utf-8') as export_file:
            export_file.writelines(f)

# Функция изменений данных
def modify_data():
    entry_num = int(input('Введите номер строки для изменения От 1 до ... : '))
    with open(filename, 'r', encoding='utf-8') as f:
        entries = f.readlines()
    if entry_num < 1 or entry_num > len(entries):
        print('Неверный номер записи')
        return

    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    patronymic = input('Введите Отчество: ')
    phone = input('Введите номер телефона: ')

    entries[entry_num - 1] = f'{surname}, {name}, {patronymic}, {phone}\n'

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(entries)

    print('Запись успешно изменена')

# Функция удаления данных           
def delete_data():
    data_num = int(input('Введите номер строки для удаления От 1 до ... : '))
    with open(filename, 'r', encoding='utf-8') as f:
        entries = f.readlines()

    if data_num < 1 or data_num > len(entries):
        print('Неверный номер записи')
        return

    del entries[data_num - 1]

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(entries)

    print('Запись успешно удалена')           


# основной цикл для отображения опций меню
def main():
    while True:
        print('1. Добавить запись')
        print('2. Показать записи')
        print('3. Поиск элементов')
        print('4. Экспорт данных')
        print('5. Изменение данных')
        print('6. Удаление данных')
        print('7. Выход')
        choice = input('Введите свой выбор: ')
        if choice == '1':
            add_data()
        elif choice == '2':
            display_data()
        elif choice == '3':
            search_data()
        elif choice == '4':
            export_data()
        elif choice == '5':
            modify_data()
        elif choice == '6':
            delete_data()
        elif choice == '7':
            break
        else:
            print('Неверный выбор. Пожалуйста, попробуйте еще раз.')

filename = 'phonebook.txt'
main()
