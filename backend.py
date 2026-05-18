import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)

# Povolenie komunikácie frontend ↔ backend
CORS(app)

# Pripojenie k PostgreSQL databáze (ponechané pôvodné údaje)
def get_db_connection():
    return psycopg2.connect(
        dbname="netusim_uz",
        user="netusim_uz_user",
        password="7qvI8csutUe7Xr5sk3i8H7BGxZLWdsoc",
        host="dpg-d7ng6tiqqhas73frvtt0-a.frankfurt-postgres.render.com",
        port=5432
    )

# TEST ROUTA
@app.route('/')
def home():
    return jsonify({
        "message": "Backend beží na Renderi!"
    })

# API ROUTA SO SORTIARANÍM CEZ DATABÁZU
@app.route('/api')
def get_all_students():

    conn = None

    try:
        # Prečítame z URL, ako chce frontend dáta zoradiť (predvolene 'az')
        sort_order = request.args.get('sort', 'az')

        conn = get_db_connection()
        cur = conn.cursor()

        # Základný SQL dopyt
        query = """
            SELECT id, name, surname, nickname, image, bio
            FROM students
        """

        # Podľa požiadavky pridáme SQL zoradenie (žiadny Python .sort())
        if sort_order == "za":
            query += " ORDER BY name DESC, surname DESC;"
        else:
            query += " ORDER BY name ASC, surname ASC;"

        cur.execute(query)
        rows = cur.fetchall()

        students = []

        # Prevod SQL dát na JSON objekty
        for row in rows:
            students.append({
                "id": row[0],
                "name": row[1],
                "surname": row[2],
                "nickname": row[3],
                "image": row[4],
                "bio": row[5]
            })

        cur.close()

        # Vracia JSON pole zoradené priamo z DB
        return jsonify(students)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

    finally:
        if conn:
            conn.close()

# Spustenie Flask servera
if __name__ == '__main__':
    app.run(debug=True)