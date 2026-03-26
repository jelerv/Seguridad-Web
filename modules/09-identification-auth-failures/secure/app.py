from flask import Flask, request, jsonify, abort
import bcrypt
import jwt
import datetime
from functools import wraps
import time

app = Flask(__name__)

SECRET_KEY = "super_strong_secret_key_2025_grok_xai_very_long_and_random_12345!"

# Base de datos simulada
users = {}
login_attempts = {}   # Para rate limiting

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Rate limiting simple
def rate_limit(max_attempts=5, window=60):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()
            if ip not in login_attempts:
                login_attempts[ip] = []
            # Limpiar intentos antiguos
            login_attempts[ip] = [t for t in login_attempts[ip] if now - t < window]
            
            if len(login_attempts[ip]) >= max_attempts:
                abort(429, description="Demasiados intentos. Intenta más tarde.")
            
            login_attempts[ip].append(now)
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/login', methods=['POST'])
@rate_limit(max_attempts=5, window=60)
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username not in users:
        return jsonify({"error": "Credenciales inválidas"}), 401
    
    if check_password(password, users[username]["password"]):
        # ✅ JWT seguro
        token = jwt.encode({
            'username': username,
            'role': users[username]["role"],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),   # Expiración corta
            'iat': datetime.datetime.utcnow()
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({"token": token})
    
    return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if len(password) < 12:
        abort(400, description="La contraseña debe tener al menos 12 caracteres")
    
    users[username] = {
        "password": hash_password(password),
        "role": "user"
    }
    return jsonify({"message": "Usuario registrado correctamente"})

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            abort(401, description="Token es requerido")
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.current_user = decoded
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            abort(401, description="Token ha expirado")
        except:
            abort(401, description="Token inválido")
    return decorated

@app.route('/api/profile')
@token_required
def profile():
    return jsonify({
        "username": request.current_user['username'],
        "role": request.current_user['role']
    })

@app.route('/api/admin')
@token_required
def admin_only():
    if request.current_user.get('role') != 'admin':
        abort(403, description="Acceso denegado")
    return jsonify({"message": "Panel de administrador"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
