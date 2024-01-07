def insert_client(conn, data_client):
    for client in data_client:
        postgres_query = """INSERT INTO clients(name, surname, email)
                            VALUES (%s,%s,%s)
                            RETURNING client_id"""
        record_to_insert = (client[0], client[1], client[2])
        with conn.cursor() as cur:
            cur.execute(postgres_query, record_to_insert)
            conn.commit()
            data = cur.fetchone()
            print(data[0], "Запись успешно добавлена в таблицу")


def add_telephone(conn, telephone, client_id):
    postgres_add_query = """INSERT INTO telephone_data(telephone, client_id) 
                            VALUES (%s, %s)"""
    record_to_add = (telephone, str(client_id))
    with conn.cursor() as cur:
        cur.execute(postgres_add_query, record_to_add)
        conn.commit()
        print(client_id, "Клиенту успешно добавлен телефон")


def delete_clients(conn, client_id):
    for id in client_id:
        postgres_query_telephone = """DELETE FROM telephone_data WHERE client_id = %s"""
        postgres_query = """DELETE FROM clients WHERE client_id = %s"""
        with conn.cursor() as cur:
            cur.execute(postgres_query_telephone, str(id))
            conn.commit()
            cur.execute(postgres_query, str(id))
            conn.commit()
            print(id, "Запись успешно удалена из таблицы клиентов, как и все его телефоны")


def delete_telephone(conn, telephone=None, client_id=None):
    if telephone == None:
        # если нет конкретного номера, то удаляем все номера клиента
        postgres_query = """DELETE FROM telephone_data WHERE client_id = %s"""
        data = (str(client_id))
    elif client_id == None:
        # удаляем тогда кокретный номер
        postgres_query = """DELETE FROM telephone_data WHERE telephone = %s"""
        data = (telephone,)
    elif telephone != None and client_id != None:
        # удаляемый определенный номер указанного клиента
        postgres_query = """DELETE FROM telephone_data WHERE telephone = %s AND client_id = %s"""
        data = (telephone, str(client_id))
    else:
        return "Не ввели необходимых данных для удаления телефона"
    with conn.cursor() as cur:
        cur.execute(postgres_query, data)
        conn.commit()


def delete_email(conn, email):
    postgres_query = """DELETE FROM email_data WHERE email = %s"""
    with conn.cursor() as cur:
        cur.execute(postgres_query, (email,))
        conn.commit()

# telephone_old  - поскольу у пользователя могут быть несколько телефонов
def update_record(conn, client_id, name = None, surname = None, email = None, telephone_new = None, telephone_old = None):
    if name != None and surname != None and email != None:
        query = """UPDATE clients SET name = %s, surname = %s, email = %s WHERE client_id = %s"""
        record = (name, surname, email, client_id,)
    elif name != None and surname != None:
        query = """UPDATE clients SET name = %s, surname = %s WHERE client_id = %s"""
        record = (name, surname, client_id,)
    elif name != None and email != None:
        query = """UPDATE clients SET name = %s, email = %s WHERE client_id = %s"""
        record = (name, email, client_id,)
    elif surname != None and email != None:
        query = """UPDATE clients SET surname = %s, email = %s WHERE client_id = %s"""
        record = (surname, email, client_id,)
    elif name != None:
        query = """UPDATE clients SET name = %s WHERE client_id = %s"""
        record = (name, client_id,)
    elif surname != None:
        query = """UPDATE clients SET surname = %s WHERE client_id = %s"""
        record = (surname, client_id,)
    elif email != None:
        query = """UPDATE clients SET email = %s WHERE client_id = %s"""
        record = (surname, client_id,)
    with conn.cursor() as cur:
        cur.execute(query, record)
        conn.commit()
    if telephone_new != None and telephone_old != None:
        query2 = """UPDATE telephone_data SET telephone = %s WHERE telephone = %s"""
        record2 =(telephone_new, telephone_old,)
        with conn.cursor() as cur:
            cur.execute(query2, record2)
            conn.commit()



def search_client(conn, name='%', surname='%', email='%', telephone='%'):
    query = """SELECT * FROM clients AS c INNER JOIN telephone_data AS t ON c.client_id = t.client_id
                WHERE c.name like %s AND c.surname like %s AND c.email like %s AND 
                      t.telephone like %s;
            """
    query_data = (name, surname, email, telephone,)
    with conn.cursor() as cur:
        cur.execute(query, query_data)
        for row in cur.fetchall():
            print("Client_id =", row[0])
            print("Name =", row[1])
            print("Surname =", row[2])
            print("Email =", row[3])
            print("Telephone =", row[4], "\n")


def select_data(conn):
    with conn.cursor() as cur:
        print('Таблица клиентов\n')
        cur.execute("""SELECT * FROM clients""")
        client_records = cur.fetchall()
        for row in client_records:
            print("Client_id =", row[0])
            print("Name =", row[1])
            print("Surname =", row[2])
            print("Email =", row[3], "\n")
        print('Таблица телефонов\n')
        cur.execute("""SELECT * FROM telephone_data""")
        client_records = cur.fetchall()
        for row in client_records:
            print("Telephone =", row[0])
            print("Client_Id =", row[1], "\n")
