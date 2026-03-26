
**vulnerable/app.py** (Autenticación insegura)
```python
from flask import Flask, request, jsonify
import jwt
import datetime
import hashlib

app = Flask(__name__)

# Base de datos simulada con contraseñas débiles
users = {
    "admin": {"password": "admin123", "role": "admin"},   # Contraseña en texto plano
    "user": {"password": "password", "role": "user"},
    "test": {"password": "123456", "role": "user"}
}

SECRET_KEY = "weaksecret"   # Clave débil y hardcodeada

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username]["password"] == password:
        # ❌ JWT inseguro: clave débil + expiración larga + sin protección
        token = jwt.encode({
            'username': username,
            'role': users[username]["role"],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)  # 7 días = muy riesgoso
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({"token": token, "message": "Login exitoso (inseguro)"})
    
    return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/api/profile')
def profile():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        # ❌ No valida correctamente el token
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256', 'none'])  # Permite "none"
        return jsonify({
            "username": decoded.get('username'),
            "role": decoded.get('role')
        })
    except:
        return jsonify({"error": "Token inválido"}), 401

@app.route('/api/admin')
def admin_only():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if decoded.get('role') != 'admin':
            return jsonify({"error": "Acceso denegado"}), 403
        return jsonify({"message": "Bienvenido al panel de administrador"})
    except:
        return jsonify({"error": "Token inválido"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
