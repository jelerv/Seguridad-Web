from flask import Flask, request, jsonify, abort
import json
import logging
from functools import wraps
import time

app = Flask(__name__)

# Logging estructurado y seguro
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Rate limiting simple
request_counts = {}

def rate_limit(max_requests=100, window=60):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()
            if ip not in request_counts:
                request_counts[ip] = []
            request_counts[ip] = [t for t in request_counts[ip] if now - t < window]
            
            if len(request_counts[ip]) >= max_requests:
                abort(429, description="Too many requests")
            request_counts[ip].append(now)
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/api/restore', methods=['POST'])
def restore_backup():
    """A08: Uso seguro de JSON en lugar de pickle"""
    if 'file' not in request.files:
        abort(400, description="No file provided")
    
    file = request.files['file']
    try:
        data = json.loads(file.read().decode('utf-8'))
        return jsonify({"status": "restored", "data": data})
    except Exception:
        logging.warning("Invalid JSON restore attempt")
        abort(400, description="Invalid data format")

@app.route('/api/user/<user_id>')
def get_user(user_id):
    """API3: Proper Object Property Level Authorization"""
    # Solo devolvemos campos permitidos según rol
    user = {
        "id": user_id,
        "name": "John Doe",
        "role": "user",
        "email": "john@example.com"
        # credit_card e is_admin NO se exponen
    }
    return jsonify(user)

@app.route('/api/calculate', methods=['POST'])
@rate_limit(max_requests=50, window=60)
def calculate():
    """A10: Manejo seguro de excepciones + rate limiting"""
    try:
        numbers = request.json.get('numbers', [])
        if len(numbers) > 1000:
            abort(400, description="Too many numbers")
        
        result = sum(int(x) for x in numbers if str(x).isdigit())
        return jsonify({"result": result})
    except ValueError:
        abort(400, description="Invalid number format")
    except Exception:
        logging.error("Unexpected error in calculate", exc_info=False)  # No exponer stack trace
        abort(500, description="Internal server error")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
