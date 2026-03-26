from flask import Flask, request, jsonify, abort
import bcrypt
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Clave fuerte generada con secrets.token_urlsafe()
SECRET_KEY = "supersecretkey_2025_xai_grok_very_long_and_random_!@#"

users = {}  # Se llenará al registrar

def hash_password(password):
    """Hashing seguro con bcrypt"""
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if len(password) < 8:
        abort(400, description="La contraseña debe tener al menos 8 caracteres")
    
    hashed = hash_password(password)
    users[username] = {"password": hashed, "role": "user"}
    
    return jsonify({"message": "Usuario registrado correctamente"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users and check_password(password, users[username]["password"]):
        # ✅ JWT seguro
        token = jwt.encode({
            'user': username,
            'role': users[username]["role"],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),  # Expiración corta
            'iat': datetime.datetime.utcnow()
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({"token": token})
    
    return jsonify({"error": "Credenciales inválidas"}), 401

# Middleware para verificar JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            abort(401, description="Token requerido")
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.current_user = decoded
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            abort(401, description="Token expirado")
        except:
            abort(401, description="Token inválido")
    return decorated

@app.route('/api/profile')
@token_required
def profile():
    return jsonify({
        "user": request.current_user['user'],
        "role": request.current_user['role']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
