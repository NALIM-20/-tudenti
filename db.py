import psycopg2

def setup_db():
    conn = psycopg2.connect(
        dbname="netusim_uz",
        user="netusim_uz_user",
        password="7qvI8csutUe7Xr5sk3i8H7BGxZLWdsoc",
        host="dpg-d7ng6tiqqhas73frvtt0-a.frankfurt-postgres.render.com",
        port=5432
    )
    cur = conn.cursor()

    # Vytvorenie tabuľky
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        nickname VARCHAR(50),
        image TEXT,
        bio TEXT
    );
    """)

    # Vymazanie a vloženie dát
    cur.execute("DELETE FROM students;")
    
    students_data = [
        (1, 'Adrian', 'Červenka', 'chilli pepper', 'https://picsum.photos/id/1011/300/200', 'Má fakt divné hlášky.'),
        (2, 'Milan', 'Kokina', 'tanečník', 'https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4', 'Nechcelo sa mi toto vobec robiť.'),
        (3, 'Martin', 'Jelínek', 'král jelimán', 'https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d', '............'),
        (4, 'Daniel', 'Barta', 'skeleton', 'https://picsum.photos/id/1014/300/200', '...........'),
        (5, 'Matej', 'Randziak', 'tankista', 'https://picsum.photos/id/1015/300/2000', '...........'),
        (6, 'Matúš', 'Bucko', 'xxxxxxxx', 'https://picsum.photos/id/1016/300/200', 'Nechcelo sa mi toto vobec robiť.'),
        (7, 'Janka', 'Vargová', 'xxxxxxxxx', 'https://picsum.photos/id/1018/300/200', 'Má fakt divné hlášky.'),
        (8, 'Matúš', 'Holečka', 'xxxxxxxxxx', 'https://picsum.photos/id/1019/300/200', '............'),
        (9, 'Marko', 'Mihalička', 'xxxxxxxxxx', 'https://picsum.photos/id/1020/300/200', '............'),
        (10, 'Lukáš', 'Vindiš', 'žirafa', 'https://picsum.photos/id/1021/300/200', '............')
    ]

    for s in students_data:
        cur.execute("INSERT INTO students (id, name, surname, nickname, image, bio) VALUES (%s, %s, %s, %s, %s, %s)", s)

    conn.commit()
    cur.close()
    conn.close()
    print("Databáza je pripravená!")

if __name__ == '__main__':
    setup_db()