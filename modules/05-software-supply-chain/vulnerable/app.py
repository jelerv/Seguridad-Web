from flask import Flask, jsonify
import requests
import jwt   # pyjwt

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Aplicación con dependencias vulnerables",
        "status": "running with outdated components"
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
