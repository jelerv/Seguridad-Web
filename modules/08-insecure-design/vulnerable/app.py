from flask import Flask, request, jsonify

app = Flask(__name__)

# Diseño inseguro: lógica de negocio frágil y sin validación profunda
orders = []

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json
    # ❌ Insecure Design:
    # 1. No valida si el usuario está autorizado para ese monto
    # 2. No tiene límite de monto por transacción
    # 3. No implementa double confirmation para compras altas
    # 4. Confía ciegamente en el precio enviado por el cliente
    
    order = {
        "user_id": data.get("user_id"),
        "product": data.get("product"),
        "price": data.get("price"),           # Precio enviado por cliente
        "quantity": data.get("quantity", 1),
        "total": data.get("price") * data.get("quantity", 1)
    }
    
    orders.append(order)
    return jsonify({"status": "order_created", "order": order})

@app.route('/api/admin/users')
def list_all_users():
    # ❌ Insecure Design: No hay control de acceso a nivel de función
    return jsonify({"users": ["admin", "user1", "user2"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
