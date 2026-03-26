**vulnerable/app.py** (Código inseguro)
```python
from flask import Flask, request, jsonify, abort
import requests

app = Flask(__name__)

# Base de datos simulada en memoria
users = {
    1: {"id": 1, "username": "admin", "role": "admin", "email": "admin@company.com", "salary": 15000},
    2: {"id": 2, "username": "user", "role": "user", "email": "user@company.com", "salary": 5000},
    3: {"id": 3, "username": "bob", "role": "user", "email": "bob@company.com", "salary": 7000}
}

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    """Vulnerable: Broken Object Level Authorization (BOLA/IDOR)"""
    if user_id not in users:
        abort(404)
    # Cualquiera puede ver cualquier usuario sin verificar ownership o permisos
    return jsonify(users[user_id])

@app.route('/api/user/<int:user_id>/role', methods=['PUT'])
def change_role(user_id):
    """Vulnerable: Privilege Escalation"""
    new_role = request.json.get('role')
    if user_id in users:
        users[user_id]['role'] = new_role
        return jsonify({"status": "success", "new_role": new_role})
    abort(404)

@app.route('/api/proxy')
def proxy():
    """Vulnerable: Server-Side Request Forgery (SSRF)"""
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "url parameter required"}), 400
    
    try:
        # Sin validación de URL → SSRF crítico
        response = requests.get(url, timeout=5, allow_redirects=False)
        return response.text, response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
