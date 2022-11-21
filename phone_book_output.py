import sqlite3 as sql

global conn
global cursor

conn = sql.connect('data_abonents.db')
cursor = conn.cursor()

def abonent_output():
    print('Введите данные абонента:\n')
    surname_output = input('Фамилия: ')
    name_output = input('Имя: ')
    patron_output = input('Отчество: ')
    print()
    
    cursor.execute(f"SELECT phone_number FROM phone_list WHERE (surname, name, patron) = ('{surname_output}', '{name_output}', '{patron_output}')")
    result = cursor.fetchall()
    if result == []:
        print('Данный абонент отсутствует в справочнике!')
    else:
        for row in result:
            print(f'Номер телефона: {row[0]}')

            