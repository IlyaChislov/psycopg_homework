import psycopg2

import functions

try:
    conn = psycopg2.connect(database='clients', user='postgres', password='postgres')
    functions.create_table(conn)
    while 1 < 2:
        print("""Выберите номер нужного запроса:\n 1.Функция, позволяющая добавить нового клиента;\n 
              2. Функция, позволяющая добавить телефон для существующего клиента;\n
              3. Функция, позволяющая изменить данные о клиенте;\n
              4. Функция, позволяющая удалить телефон для существующего клиента;\n
              5. Функция, позволяющая удалить существующего клиента;\n
              6. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.\n
              7. Показать все данные.\n
              8. Выйти из программы""")
        num = int(input())
        if num == 1:
            functions.insert_client(conn)
        elif num == 2:
            functions.add_telephone(conn)
        elif num == 3:
            functions.update_record(conn)
        elif num == 4:
            functions.delete_telephone(conn)
        elif num == 5:
            functions.delete_clients(conn)
        elif num == 6:
            functions.search_client(conn)
        elif num == 7:
            functions.select_data(conn)
        elif num == 8:
            break
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        conn.close()
        print("Соединение с PostgreSQL закрыто")
