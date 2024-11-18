import sqlite3
from flask import Flask, jsonify, request, g

#Comentario de prueba

app = Flask(__name__)
DATABASE = 'database.db'  # Nombre del archivo de la base de datos

# Conexión a la base de datos
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Crear la tabla de usuarios si no existe
def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL)''')
        db.commit()

# Cerrar la conexión cuando se cierre la aplicación
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Ruta de prueba para verificar que el microservicio funcione
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Microservicio de usuarios funcionando correctamente"}), 200

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    db = get_db()
    cursor = db.execute('SELECT id, nombre FROM usuarios')
    usuarios = [{"id": row[0], "nombre": row[1]} for row in cursor.fetchall()]
    return jsonify(usuarios), 200

# Obtener un usuario específico por ID
@app.route('/usuarios/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    db = get_db()
    cursor = db.execute('SELECT id, nombre FROM usuarios WHERE id = ?', (user_id,))
    usuario = cursor.fetchone()
    if usuario:
        return jsonify({"id": usuario[0], "nombre": usuario[1]}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

# Crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    if "nombre" not in data:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    db = get_db()
    cursor = db.execute('INSERT INTO usuarios (nombre) VALUES (?)', (data["nombre"],))
    db.commit()
    new_id = cursor.lastrowid
    return jsonify({"id": new_id, "nombre": data["nombre"]}), 201

# Actualizar un usuario existente
@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def update_usuario(user_id):
    data = request.get_json()
    if "nombre" not in data:
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
    db = get_db()
    cursor = db.execute('UPDATE usuarios SET nombre = ? WHERE id = ?', (data["nombre"], user_id))
    db.commit()
    if cursor.rowcount == 0:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"id": user_id, "nombre": data["nombre"]}), 200

# Eliminar un usuario
@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def delete_usuario(user_id):
    db = get_db()
    cursor = db.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    db.commit()
    if cursor.rowcount == 0:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado"}), 200

if __name__ == '__main__':
    init_db()  # Inicializar la base de datos al iniciar la aplicación
    app.run(host='0.0.0.0', port=5001)
