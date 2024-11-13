from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/publications', methods=['GET'])
def get_publications():
    publications = [
        {"id": 1, "title": "My first post", "content": "This is my first post", "user_id": 101},
        {"id": 2, "title": "Hello World!", "content": "Learning microservices with Flask.", "user_id": 102},
    ]
    return jsonify(publications)

@app.route('/publications', methods=['POST'])
def create_publication():
    data = request.json
    # Aquí se añadiría lógica para crear y almacenar una publicación
    return jsonify({"message": "Publication created", "data": data}), 201

if __name__ == '__main__':
    app.run(port=5002)  # Asegúrate de que el puerto no esté en uso y de que sea diferente al de otros microservicios
