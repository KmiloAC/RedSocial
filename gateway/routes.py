# gateway/routes.py
from flask import Blueprint, request, jsonify
import requests
from config import MICROSERVICIO_USUARIOS, MICROSERVICIO_PUBLICACIONES, MICROSERVICIO_NOTIFICACIONES

# Definimos el Blueprint para el API Gateway
gateway = Blueprint('gateway', __name__)

# Ruta para redirigir solicitudes al microservicio de usuarios
@gateway.route('/usuarios/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_usuarios(path):
    url = f"{MICROSERVICIO_USUARIOS}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json() if request.method in ['POST', 'PUT'] else None  # Enviar JSON solo en caso de POST o PUT
    )
    return jsonify(response.json()), response.status_code

# (Opcional) Ruta para redirigir al microservicio de publicaciones
@gateway.route('/publicaciones/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_publicaciones(path):
    url = f"{MICROSERVICIO_PUBLICACIONES}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json() if request.method in ['POST', 'PUT'] else None
    )
    return jsonify(response.json()), response.status_code

# (Opcional) Ruta para redirigir al microservicio de notificaciones
@gateway.route('/notificaciones/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_notificaciones(path):
    url = f"{MICROSERVICIO_NOTIFICACIONES}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json() if request.method in ['POST', 'PUT'] else None
    )
    return jsonify(response.json()), response.status_code
