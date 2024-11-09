from flask import Flask, jsonify

app = Flask(__name__)

# Ruta de prueba para verificar que el microservicio funcione
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Microservicio de usuarios funcionando correctamente"}), 200

# Otra ruta de ejemplo para manejar usuarios (puedes ampliarla según las funcionalidades que necesites)
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    # Esta es una lista de ejemplo
    usuarios = [
        {"id": 1, "nombre": "Alice"},
        {"id": 2, "nombre": "Bob"}
    ]
    return jsonify(usuarios), 200

if __name__ == '__main__':
    # Ejecuta el microservicio en el puerto 5001
    app.run(host='0.0.0.0', port=5001)
