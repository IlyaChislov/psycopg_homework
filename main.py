import psycopg2

import functions
import create_tables

def get_connection():
    try:
        conn = psycopg2.connect(database='clients', user='postgres', password='postgres')
        return conn
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

conn = get_connection()
#Создаем таблицы
create_tables.create_t(conn)
# Вывод имеющихся данных
functions.select_data(conn)
# Заполняем таблицы
# Добавим в таблицу clients следующих клиентов
# data_clients = [['Михаил', 'Бычков', 'buchka@mail.ru'], ['Руслан', 'Беликов', 'belgram@yandex.ru'], ['Илья', 'Числов', 'il.spartak@yandex'], ['Илья', 'Лебедев', 'lebebed@yandex.ru'], ['Фёдор', 'Пономарёв', 'poker@yandex.ru']]
# functions.insert_client(conn, data_clients)
# Добавляем телефоны
# functions.add_telephone(conn,'89536162332', 1)
# functions.add_telephone(conn, '89532214251', 2)
# functions.add_telephone(conn, '89606504113', 2)
# functions.add_telephone(conn, '89092290446', 3)
# functions.add_telephone(conn,  '89606442571', 4)
# functions.add_telephone(conn,  '89192345423', 4)
# functions.add_telephone(conn, '82321234324', 5)
# functions.add_telephone(conn, '82321239999', 6)
# functions.add_telephone(conn, '82321236666', 6)
# functions.add_telephone(conn, '82321235555', 6)
# Удалим из таблицы clients клиентов со следующими id:
# client_id=[5]
# functions.delete_clients(conn, client_id)
# functions.select_data(conn)
# Удалим номер телефона - можно удалять как конкретный номер, так и все номера клиента:
# functions.delete_telephone(conn, '82321239999')
# functions.delete_telephone(conn, '82321236666', 6)
# functions.delete_telephone(conn, client_id=6)
# functions.select_data(conn)
# Поиск клиентов по разным параметрам
# functions.search_client(conn, 'Руслан')
# functions.search_client(conn, 'Михаил', 'Бычков', 'buchka@mail.ru')
# functions.search_client(conn, 'Илья', 'Числов', 'il.spartak@yandex', '89092290446')
# Изменение данных о клиенте
functions.update_record(conn, '1', 'Михаил', 'Бычковвв','bychkov@gmail.com', '89521237856','8888')
functions.select_data(conn)