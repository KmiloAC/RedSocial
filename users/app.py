from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de usuarios de ejemplo (simulando una base de datos en memoria)
usuarios = [
    {"id": 1, "nombre": "Alice"},
    {"id": 2, "nombre": "Bob"}
]

# Ruta de prueba para verificar que el microservicio funcione
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Microservicio de usuarios funcionando correctamente"}), 200

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios), 200

# Obtener un usuario específico por ID
@app.route('/usuarios/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    usuario = next((u for u in usuarios if u["id"] == user_id), None)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

# Crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    if "nombre" not in data:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400

    new_id = max(u["id"] for u in usuarios) + 1 if usuarios else 1
    nuevo_usuario = {"id": new_id, "nombre": data["nombre"]}
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

# Actualizar un usuario existente
@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def update_usuario(user_id):
    data = request.get_json()
    usuario = next((u for u in usuarios if u["id"] == user_id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    if "nombre" in data:
        usuario["nombre"] = data["nombre"]
    return jsonify(usuario), 200

# Eliminar un usuario
@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def delete_usuario(user_id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != user_id]
    return jsonify({"message": "Usuario eliminado"}), 200

if __name__ == '__main__':
    # Ejecuta el microservicio en el puerto 5001
    app.run(host='0.0.0.0', port=5001)
