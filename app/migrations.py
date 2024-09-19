from app.db import get_connection


def migrate():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY, 
        username varchar(100), 
        password varchar(255),
        refresh_token varchar(255)
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS notes (
        id serial PRIMARY KEY,
        text TEXT,
        user_id int,
        CONSTRAINT user_id
            FOREIGN KEY (user_id)
                REFERENCES users(id)
    );""")

    conn.commit()

    cur.close()
    conn.close()
