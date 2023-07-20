import sqlite3
import sys


def create_db_and_table():
    conn = sqlite3.connect('aygyun.salim-food.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS food (
                            code TEXT,
                            descript TEXT,
                            nmbr INTEGER,
                            nutname TEXT,
                            retention REAL)
                            ''')
    conn.commit()
    return conn


def insert_data(conn):
    with open('retn5_dat.txt', 'r') as file:
        for line in file:
            columns = line.strip().split('^')
            code, descript, nmbr, nutname, retention = [col.strip('~') for col in columns[:5]]
            conn.execute("INSERT INTO food (code, descript, nmbr, nutname, retention) VALUES (?, ?, ?, ?, ?)",
                         (code, descript, nmbr, nutname, retention))
    conn.commit()


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result



def fetch_all_rows(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food")
    rows = cursor.fetchall()
    return rows


def print_rows(rows):
    print("code | descript | nmbr | nutname | retention")
    print("-" * 51)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")


def main():
    conn = create_db_and_table()
    insert_data(conn)

    rows = fetch_all_rows(conn)
    # print_rows(rows)

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        result = execute_query(conn, query)
        print(result)

    conn.close()

if __name__ == '__main__':
    main()
