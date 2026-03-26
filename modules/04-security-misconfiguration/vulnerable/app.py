
**vulnerable/app.py** (Código inseguro)
```python
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Datos de ejemplo
data = {"users": ["admin", "user1", "user2"], "secret_key": "supersecret123"}

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido - Aplicación con misconfiguraciones"})

@app.route('/api/data')
def get_data():
    """Vulnerable: CORS amplio + información sensible"""
    return jsonify(data)

@app.route('/admin')
def admin():
    """Vulnerable: Ruta administrativa sin protección"""
    return jsonify({
        "status": "ok",
        "admin_panel": "accessible",
        "server_path": "/app",
        "python_version": "3.11",
        "debug_mode": True
    })

@app.route('/.env')
def env_file():
    """Vulnerable: Exposición de archivo sensible"""
    return "DB_PASSWORD=ProductionSecret123\nAPI_KEY=sk_live_1234567890"

# Error handler que muestra información detallada (muy peligroso)
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "Not Found",
        "path": request.path,
        "method": request.method,
        "possible_routes": ["/", "/api/data", "/admin"]
    }), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": str(e), "traceback": "Stack trace would be here"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Debug activado = muy peligroso
