from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(':memory:')
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT
        );
        INSERT INTO users (username, password, email) VALUES 
            ('admin', 'admin123', 'admin@company.com'),
            ('user', 'password', 'user@company.com'),
            ('guest', 'guest123', 'guest@company.com');
    ''')
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # ❌ VULNERABLE: Concatenación directa de SQL
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return jsonify({"status": "success", "message": f"Bienvenido {user[1]}"})
    return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

@app.route('/search')
def search():
    q = request.args.get('q', '')
    
    # ❌ VULNERABLE: Concatenación en búsqueda
    query = f"SELECT id, username, email FROM users WHERE username LIKE '%{q}%' OR email LIKE '%{q}%'"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return jsonify([{"id": r[0], "username": r[1], "email": r[2]} for r in results])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
