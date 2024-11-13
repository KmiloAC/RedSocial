# gateway/routes.py
from flask import Blueprint, request, jsonify
import requests
from config import MICROSERVICIO_USUARIOS, MICROSERVICIO_NOTIFICACIONES 

# Creamos un Blueprint para organizar las rutas
gateway = Blueprint('gateway', __name__)

# Ruta estática para manejar /usuarios
@gateway.route('/usuarios', methods=['GET', 'POST'])
def handle_usuarios_root():
    url = f"{MICROSERVICIO_USUARIOS}/usuarios"
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
    url = f"{MICROSERVICIO_USUARIOS}/usuarios/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.get_json() if request.method in ['POST', 'PUT'] else None
    )
    return jsonify(response.json()), response.status_code

# Ruta para el microservicio de notificaciones
@gateway.route('/notifications', methods=['POST'])
def handle_notifications():
    url = f"{MICROSERVICIO_NOTIFICACIONES}/notifications/send"
    try:
        response = requests.post(url, json=request.get_json(), headers=request.headers)
        response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error HTTP
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        # Manejo de error en caso de fallo de la solicitud
        return jsonify({"error": str(e)}), 500

# Ruta para obtener el historial de notificaciones
@gateway.route('/notifications/history/<user_id>', methods=['GET'])
def handle_notifications_history(user_id):
    url = f"{MICROSERVICIO_NOTIFICACIONES}/notifications/history/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error HTTP
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        # Manejo de error en caso de fallo de la solicitud
        return jsonify({"error": str(e)}), 500
