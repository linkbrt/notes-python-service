import psycopg2

from db import get_connection


def migrate():
    conn = get_connection()
    cur = conn.cursor()
    # cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer, data varchar);")

    # cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
                # (100, "abcdef"))
    cur.execute("SELECT * FROM test;")
    print(cur.fetchall())

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    migrate()