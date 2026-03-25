from flask import Flask, request, jsonify, abort
import requests
from functools import wraps

app = Flask(__name__)

# Simulación de usuario actual (en producción usa JWT u OAuth)
def get_current_user():
    return {"id": 2, "role": "user"}

def has_access(current_user, target_id):
    if current_user["role"] == "admin":
        return True
    return current_user["id"] == target_id

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    current = get_current_user()
    if not has_access(current, user_id):
        abort(403)
    # ... resto del código seguro
    return jsonify({"message": "Access granted"})

@app.route('/api/proxy')
def proxy():
    url = request.args.get('url')
    # Mitigación SSRF: whitelist de dominios permitidos
    allowed_domains = ["api.trusted.com", "internal.trusted.local"]
    if not any(domain in url for domain in allowed_domains):
        abort(403)
    # ... resto
