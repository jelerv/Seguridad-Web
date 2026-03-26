from flask import Flask, request, jsonify, abort
from functools import wraps

app = Flask(__name__)

# Simulación de usuario actual (en producción viene de JWT)
def get_current_user():
    return {"id": 2, "role": "user", "max_order_amount": 5000}

def requires_role(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if get_current_user()["role"] != role:
                abort(403, description="Insufficient privileges")
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json
    user = get_current_user()
    
    total = float(data.get("price", 0)) * int(data.get("quantity", 1))
    
    # ✅ Controles de diseño seguro:
    if total > user["max_order_amount"]:
        abort(400, description="Order amount exceeds user limit. Requires approval.")
    
    if total > 1000:
        # Simula double confirmation o aprobación adicional
        print(f"High value order detected: ${total} - Requires additional verification")
    
    order = {
        "user_id": user["id"],
        "product": data.get("product"),
        "price": data.get("price"),
        "quantity": data.get("quantity", 1),
        "total": total,
        "status": "pending_approval" if total > 1000 else "confirmed"
    }
    
    return jsonify({"status": "order_processed", "order": order})

@app.route('/api/admin/users')
@requires_role("admin")
def list_all_users():
    # ✅ Control de acceso a nivel de función
    return jsonify({"users": ["admin", "user1", "user2"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
