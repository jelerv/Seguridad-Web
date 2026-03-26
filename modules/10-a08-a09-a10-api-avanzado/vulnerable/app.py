**vulnerable/app.py** (Combinación de vulnerabilidades A08, A09, A10)
```python
from flask import Flask, request, jsonify
import pickle
import logging
import os

app = Flask(__name__)

# Configuración de logging insegura
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/api/restore', methods=['POST'])
def restore_backup():
    """A08: Deserialización insegura con pickle"""
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    try:
        # ❌ Muy peligroso: deserialización de pickle
        data = pickle.loads(file.read())
        return jsonify({"status": "restored", "data": data})
    except Exception as e:
        logging.error(f"Error restoring: {str(e)}")  # A09: Logging inseguro
        return jsonify({"error": str(e)}), 500

@app.route('/api/user/<user_id>')
def get_user(user_id):
    """API3: Broken Object Property Level Authorization"""
    user = {
        "id": user_id,
        "name": "John Doe",
        "role": "user",
        "email": "john@example.com",
        "is_admin": False,          # Campo oculto
        "credit_card": "4111-1111-1111-1111"  # Datos sensibles
    }
    return jsonify(user)   # Expone todo sin filtrado

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """A10 + API4: Mishandling + Unrestricted Resource Consumption"""
    try:
        numbers = request.json.get('numbers', [])
        # Sin límite de tamaño → posible DoS
        result = sum(int(x) for x in numbers)
        return jsonify({"result": result})
    except Exception as e:
        # A10: Excepción mal manejada - revela información interna
        return jsonify({"error": str(e), "trace": "Full stack trace would be here"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
