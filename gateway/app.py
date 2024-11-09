# gateway/app.py
from flask import Flask, request, jsonify
import requests
from config import MICROSERVICIO_USUARIOS

app = Flask(__name__)

# Ruta de prueba para redirigir a un microservicio
@app.route('/usuarios/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_usuarios(path):
    url = f"{MICROSERVICIO_USUARIOS}/{path}"
    
    # Configura los parámetros para la solicitud al microservicio
    if request.method in ['POST', 'PUT']:
        # Solo envía JSON en solicitudes POST o PUT
        response = requests.request(
            method=request.method,
            url=url,
            json=request.get_json()  # Enviar JSON solo en caso de POST o PUT
        )
    else:
        # Para GET y DELETE, no envíes JSON
        response = requests.request(
            method=request.method,
            url=url
        )
    
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000)
