from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Crear base de datos y datos de prueba
with app.app_context():
    db.engine.executescript('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT
        );
        INSERT INTO users (username, password, email) VALUES 
            ('admin', 'admin123', 'admin@company.com'),
            ('user', 'password', 'user@company.com');
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # ✅ SEGURO: Query parametrizada
    query = text("SELECT * FROM users WHERE username = :username AND password = :password")
    
    result = db.session.execute(query, {"username": username, "password": password})
    user = result.fetchone()
    
    if user:
        return jsonify({"status": "success", "message": f"Bienvenido {user.username}"})
    return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

@app.route('/search')
def search():
    q = request.args.get('q', '')
    
    # ✅ SEGURO: Parámetros + LIKE seguro
    if not q or len(q) > 50:  # Validación básica adicional
        return jsonify([])
    
    query = text("SELECT id, username, email FROM users WHERE username LIKE :q OR email LIKE :q")
    result = db.session.execute(query, {"q": f"%{q}%"})
    
    users = [{"id": row.id, "username": row.username, "email": row.email} for row in result]
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # debug=False en producción
