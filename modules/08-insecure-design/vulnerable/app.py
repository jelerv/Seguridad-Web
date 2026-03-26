from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json or {}
    
    # ❌ Decisiones de diseño inseguras:
    # 1. Confía ciegamente en los datos enviados por el cliente (precio)
    # 2. No valida límites de negocio (monto máximo por orden)
    # 3. No requiere confirmación para compras de alto valor
    # 4. No verifica si el usuario tiene saldo o permisos suficientes
    
    order = {
        "user_id": data.get("user_id"),
        "product_id": data.get("product_id"),
        "price": data.get("price"),           # Precio controlado por el cliente
        "quantity": data.get("quantity", 1),
        "total": float(data.get("price", 0)) * int(data.get("quantity", 1))
    }
    
    orders.append(order)
    return jsonify({"status": "success", "order": order, "message": "Orden creada sin validaciones de negocio"})

@app.route('/api/admin/all-orders')
def get_all_orders():
    # ❌ Insecure Design: Cualquiera puede ver todas las órdenes
    return jsonify({"orders": orders})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
