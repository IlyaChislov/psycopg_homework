def del_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
                    DROP TABLE IF EXISTS telephone_data, email_data, clients;
                    """)
        conn.commit()


def create_t(conn):
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS clients(
                        client_id SERIAL PRIMARY KEY,
                        name VARCHAR(60) NOT NULL,
                        surname VARCHAR(60) NOT NULL,
                        email VARCHAR(60) NOT NULL UNIQUE);
                    """)
        conn.commit()
        cur.execute("""CREATE TABLE IF NOT EXISTS telephone_data(
                        telephone VARCHAR(60) NOT NULL UNIQUE PRIMARY KEY,
                        client_id INTEGER NOT NULL REFERENCES clients(client_id));
                    """)
        conn.commit()
    print('Таблицы успешно созданы')
