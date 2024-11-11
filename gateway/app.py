from flask import Flask, request, jsonify
import requests
from config import MICROSERVICIO_USUARIOS

app = Flask(__name__)

# Ruta estática para manejar /usuarios
@app.route('/usuarios', methods=['GET', 'POST'])
def handle_usuarios_root():
    url = f"{MICROSERVICIO_USUARIOS}/usuarios"  # El microservicio de usuarios está escuchando en /usuarios
    # Realiza la solicitud hacia el microservicio de usuarios
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json() if request.method in ['POST', 'PUT'] else None
    )
    return jsonify(response.json()), response.status_code

# Ruta dinámica para manejar subrutas dentro de /usuarios
@app.route('/usuarios/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_usuarios(path):
    url = f"{MICROSERVICIO_USUARIOS}/usuarios/{path}"  # Redirige las subrutas hacia el microservicio
    # Realiza la solicitud hacia el microservicio de usuarios
    if request.method in ['POST', 'PUT']:
        # Si la solicitud es POST o PUT, se envía el JSON
        response = requests.request(
            method=request.method,
            url=url,
            headers=request.headers,
            json=request.get_json()  # Enviar el JSON en el cuerpo
        )
    else:
        # Para GET y DELETE, no se envía JSON
        response = requests.request(
            method=request.method,
            url=url,
            headers=request.headers
        )
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    # Ejecuta el API Gateway en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
