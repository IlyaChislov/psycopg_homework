import psycopg2


def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS clients(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(60) NOT NULL,
                        surname VARCHAR(60) NOT NULL,
                        email VARCHAR(60) NOT NULL,
                        telephone VARCHAR(60));
                    """)
        conn.commit()
    print('Таблица успешно создана')


def insert_client(conn):
    print("Введите имя клиента")
    name = str(input())
    print("Введите фамилию клиента")
    surname = str(input())
    print("Введите эмэйл клиента")
    email = str(input())
    print("Введите телефон клиента")
    telephone = str(input())
    postgres_insert_query = """ INSERT INTO clients(name, surname, email, telephone)
                                           VALUES (%s,%s,%s, %s)"""
    record_to_insert = (name, surname, email, telephone)
    with conn.cursor() as cur:
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        count = cur.rowcount
        print(count, "Запись успешно добавлена в таблицу")

def add_telephone(conn):
    print('Введите номер клиента, которому внеести телефон')
    id_client=int(input())
    print('Введите номер телефона')
    telephone=str(input())
    postgres_add_query="""UPDATE clients SET telephone = %s WHERE id = %s"""
    record_to_add=(telephone, id_client)
    with conn.cursor() as cur:
        cur.execute(postgres_add_query, record_to_add)
        conn.commit()

def update_record(conn):
    print('Введите номер клиента, данные оторого планируете изменить')
    id_client=int(input())
    print("Введите имя клиента")
    name = str(input())
    print("Введите фамилию клиента")
    surname = str(input())
    print("Введите эмэйл клиента")
    email = str(input())
    print("Введите телефон клиента")
    telephone = str(input())
    postgres_update_query="""UPDATE clients SET name = %s, surname = %s, email = %s, telephone = %s WHERE id = %s"""
    record_to_update=(name, surname, email, telephone, id_client)
    with conn.cursor() as cur:
        cur.execute(postgres_update_query, record_to_update)
        conn.commit()

def delete_telephone(conn):
    print('Введите номер клиента, которому удалить телефон')
    id_client=str(input())
    postgres_del_phone_query="""UPDATE clients SET telephone = '' WHERE id = %s"""
    with conn.cursor() as cur:
        cur.execute(postgres_del_phone_query, id_client)
        conn.commit()

def delete_clients(conn):
    print('Введите номер клиента, которого удалить из БД')
    id_client=int(input())
    delete_query = """DELETE FROM clients WHERE id = %s"""
    with conn.cursor() as cur:
        cur.execute(delete_query, id_client)
        conn.commit()

def search_client(conn):
    print('Введите имя/фамилию/почту/телефон клиента, которого надо найти')
    info=str(input())
    query="""SELECT * FROM clients WHERE name = %s OR surname = %s OR email = %s OR telephone = %s"""
    query_data=(info, info, info, info)
    with conn.cursor() as cur:
        cur.execute(query, query_data)
        print(cur.fetchall())

def select_data(conn):
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM clients""")
        client_records=cur.fetchall()
        for row in client_records:
            print("Id =", row[0], )
            print("Name =", row[1])
            print("Surname =", row[2])
            print("Email =", row[3])
            print("Telephone =", row[4], "\n")