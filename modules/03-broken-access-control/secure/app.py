from flask import Flask, request, jsonify, abort
import requests
from functools import wraps

app = Flask(__name__)

# Base de datos simulada
users = {
    1: {"id": 1, "username": "admin", "role": "admin", "email": "admin@company.com", "salary": 15000},
    2: {"id": 2, "username": "user", "role": "user", "email": "user@company.com", "salary": 5000},
    3: {"id": 3, "username": "bob", "role": "user", "email": "bob@company.com", "salary": 7000}
}

# Simulación de usuario actual (en producción usar JWT o sesión)
def get_current_user():
    # En un lab real se obtendría del token JWT o header Authorization
    return {"id": 2, "role": "user"}   # Cambia a "admin" para probar privilegios

def is_admin():
    return get_current_user()["role"] == "admin"

def has_access(target_user_id):
    current = get_current_user()
    if is_admin():
        return True
    return current["id"] == target_user_id

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    """Seguro: Verifica ownership y permisos"""
    if user_id not in users:
        abort(404)
    
    if not has_access(user_id):
        abort(403, description="Access denied")
    
    # Evitamos exponer campos sensibles (ej. salary) a usuarios normales
    user_data = users[user_id].copy()
    if not is_admin():
        user_data.pop('salary', None)
    
    return jsonify(user_data)

@app.route('/api/user/<int:user_id>/role', methods=['PUT'])
def change_role(user_id):
    """Seguro: Solo admins pueden cambiar roles"""
    if not is_admin():
        abort(403, description="Only admins can change roles")
    
    new_role = request.json.get('role')
    if user_id in users:
        users[user_id]['role'] = new_role
        return jsonify({"status": "success", "new_role": new_role})
    abort(404)

@app.route('/api/proxy')
def proxy():
    """Seguro: SSRF mitigado con allowlist"""
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "url parameter required"}), 400

    # Allowlist de dominios permitidos
    allowed_domains = [
        "api.trusted.com",
        "internal.trusted.local",
        "169.254.169.254"  # Solo si es necesario y controlado
    ]
    
    if not any(domain in url for domain in allowed_domains):
        abort(403, description="SSRF protection: URL not allowed")
    
    try:
        response = requests.get(url, timeout=3, allow_redirects=False)
        return response.text, response.status_code
    except Exception:
        return jsonify({"error": "Request failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
