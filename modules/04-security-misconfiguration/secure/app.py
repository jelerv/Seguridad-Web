from flask import Flask, request, jsonify, abort
from flask_talisman import Talisman

app = Flask(__name__)

# Configuración de seguridad con Talisman (headers recomendados)
talisman = Talisman(app,
    content_security_policy={
        'default-src': ["'self'"],
        'script-src': ["'self'"],
        'style-src': ["'self'"],
    },
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    x_frame_options='DENY',
    x_content_type_options=True,
    referrer_policy='strict-origin-when-cross-origin'
)

# Datos seguros (sin exponer información sensible)
data = {"message": "Datos públicos", "count": 42}

@app.route('/')
def home():
    return jsonify({"message": "Aplicación con configuración segura"})

@app.route('/api/data')
def get_data():
    """Seguro: CORS restringido + sin datos sensibles"""
    # CORS se maneja manualmente o con extensión
    origin = request.headers.get('Origin')
    allowed_origins = ['http://localhost:3000', 'https://trusted-frontend.com']
    
    response = jsonify(data)
    if origin in allowed_origins:
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    else:
        response.headers['Access-Control-Allow-Origin'] = 'null'
    
    return response

@app.route('/admin')
def admin():
    """Seguro: Ruta protegida"""
    abort(403, description="Access denied")

@app.errorhandler(404)
def not_found(e):
    """Errores genéricos (sin información sensible)"""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    """Errores genéricos en producción"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # Debug desactivado
