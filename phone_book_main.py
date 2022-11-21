import sqlite3 as sql
from phone_book_input import data_input
from phone_book_delete import delete_abonent
from phone_book_output import abonent_output

print()
print('МЕНЮ СПРАВОЧНИКА\n')
menu = input('Выберите, какое действие выполнить:\n "1" - Найти, "2" - Добавить, "3" - Удалить\n')
if menu == '1':
    abonent_output()
elif menu == '2':
    data_input()
elif menu == '3':
    delete_abonent()
    
else:
    print('Вы ввели неверный индекс меню!')    