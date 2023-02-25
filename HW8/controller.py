import json
import model_make_entry as mk_en
import model_edit_entry as mk_ed
import model_print as mk_pr
import model_search as mk_sr
import os
print(os.getcwd())
os.chdir("HW\HW8")

db_path = 'BD.json'
welcome = 'Enter command:\n| 1 - read & show \n| 2 - add record \n| 3 - search \n| 4 - edit or delete \n| 5 - save \n| q - Quit (without save) \n|qs - Save and Quit \n'


def load_db(path):
    # загрузить из json
    with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успешно загружена')
    return BD_local


def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        # преобразовываем словарь data в unicode-строку и записываем в файл
        fh.write(json.dumps(db, ensure_ascii=False))
    print('БД успешно сохранена')


try:
    phone_book = load_db(db_path)
except:
    phone_book = {
        'Миша гараж': {'phone': ['72443351195', '72627397543'], 'birthday': "26.01.1901", 'email': "mail@mail.ru"},
        "Ivan": {"phone": ["75864", "5005", "001", "125"], "birthday": "N/A", "email": "N/A"}}
    print("Файл ее найден! создана тестовая база данных!")

mk_pr.print_book(phone_book)
action = ''

while action != 'q' and action != 'qs':
    action = input(f'{welcome}').lower()
    if action == '1':
        mk_pr.print_book(phone_book)
    elif action == '2':
        mk_en.new_record(phone_book)
    elif action == '3':
        mk_sr.search_value(phone_book)
    elif action == '4':
        mk_ed.edit_record(phone_book)
    elif action == '5':
        save_db(db_path, phone_book)
    elif action == 'qs':
        save_db(db_path, phone_book)
        print("Good bye")
    elif action == 'q':
        print("Good bye")
    else:
        print("Wrong command")
