# routes.py
from flask import Blueprint, request, jsonify
import requests
from config import MICROSERVICIO_USUARIOS, MICROSERVICIO_PUBLICACIONES, MICROSERVICIO_NOTIFICACIONES

# Definimos el Blueprint para organizar las rutas
gateway = Blueprint('gateway', __name__)

# Ruta para el microservicio de usuarios
@gateway.route('/usuarios/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_usuarios(path):
    url = f"{MICROSERVICIO_USUARIOS}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json()
    )
    return jsonify(response.json()), response.status_code

# Ruta para el microservicio de publicaciones
@gateway.route('/publicaciones/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_publicaciones(path):
    url = f"{MICROSERVICIO_PUBLICACIONES}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json()
    )
    return jsonify(response.json()), response.status_code

# Ruta para el microservicio de notificaciones
@gateway.route('/notificaciones/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_notificaciones(path):
    url = f"{MICROSERVICIO_NOTIFICACIONES}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json()
    )
