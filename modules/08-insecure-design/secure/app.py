from flask import Flask, request, jsonify, abort
from functools import wraps

app = Flask(__name__)

orders = []

def get_current_user():
    # Simulación - en producción viene de JWT
    return {"id": 2, "role": "user", "max_order_amount": 5000}

def requires_role(required_role):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = get_current_user()
            if user["role"] != required_role:
                abort(403, description="Permisos insuficientes")
            return f(*args, **kwargs)
        return decorated
    return decorator

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json or {}
    user = get_current_user()
    
    price = float(data.get("price", 0))
    quantity = int(data.get("quantity", 1))
    total = price * quantity
    
    # ✅ Controles de diseño seguro:
    if total > user["max_order_amount"]:
        abort(400, description=f"Monto máximo por orden es ${user['max_order_amount']}. Requiere aprobación especial.")
    
    if total > 2000:
        # Requiere doble confirmación o aprobación manual (lógica de negocio segura)
        print(f"⚠️ Orden de alto valor (${total}) detectada - Requiere verificación adicional")
    
    order = {
        "user_id": user["id"],
        "product_id": data.get("product_id"),
        "price": price,
        "quantity": quantity,
        "total": total,
        "status": "pending_approval" if total > 2000 else "confirmed"
    }
    
    orders.append(order)
    return jsonify({"status": "success", "order": order})

@app.route('/api/admin/all-orders')
@requires_role("admin")
def get_all_orders():
    # ✅ Acceso controlado por rol desde el diseño
    return jsonify({"orders": orders, "count": len(orders)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
