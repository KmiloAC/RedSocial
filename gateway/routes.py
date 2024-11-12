# gateway/routes.py
from flask import Blueprint, request, jsonify
import requests
from config import MICROSERVICIO_USUARIOS

# Creamos un Blueprint para organizar las rutas
gateway = Blueprint('gateway', __name__)

# Ruta estática para manejar /usuarios
@gateway.route('/usuarios', methods=['GET', 'POST'])
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
@gateway.route('/usuarios/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
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

# Aquí puedes agregar más rutas para otros microservicios, como publicaciones y notificaciones
