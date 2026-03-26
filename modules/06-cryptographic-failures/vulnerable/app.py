
**vulnerable/app.py** (Código con fallos criptográficos)
```python
from flask import Flask, request, jsonify
import hashlib
import jwt
import datetime

app = Flask(__name__)

# Base de datos simulada con contraseñas inseguras
users = {
    "admin": {
        "password": hashlib.md5("admin123".encode()).hexdigest(),  # MD5 - Muy débil
        "role": "admin"
    },
    "user": {
        "password": hashlib.sha1("password".encode()).hexdigest(),  # SHA1 - Débil
        "role": "user"
    }
}

SECRET_KEY = "secret"  # Clave débil y hardcodeada

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # ❌ Almacenamiento inseguro
    hashed = hashlib.md5(password.encode()).hexdigest()
    users[username] = {"password": hashed, "role": "user"}
    
    return jsonify({"message": "Usuario registrado (inseguro)"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users:
        input_hash = hashlib.md5(password.encode()).hexdigest()
        if input_hash == users[username]["password"]:
            # ❌ JWT con algoritmo débil y clave estática
            token = jwt.encode({
                'user': username,
                'role': users[username]["role"],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
            }, SECRET_KEY, algorithm='HS256')
            
            return jsonify({"token": token})
    
    return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/api/profile')
def profile():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({"user": decoded['user'], "role": decoded['role']})
    except:
        return jsonify({"error": "Token inválido"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
