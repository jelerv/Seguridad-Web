from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

users = {
    1: {"id": 1, "name": "admin", "role": "admin", "email": "admin@company.com"},
    2: {"id": 2, "name": "user", "role": "user", "email": "user@company.com"}
}

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    # Vulnerable: BOLA - cualquiera puede ver cualquier usuario
    return jsonify(users.get(user_id, {"error": "Not found"}))

@app.route('/api/proxy')
def proxy():
    url = request.args.get('url')
    if url:
        try:
            r = requests.get(url, timeout=3)  # SSRF vulnerable
            return r.text
        except:
            return "Request failed"
    return "No URL provided"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
