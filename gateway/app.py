# gateway/app.py
from flask import Flask
from routes import gateway  # Importa el Blueprint desde routes.py

app = Flask(__name__)
app.register_blueprint(gateway)  # Registra el Blueprint

if __name__ == '__main__':
    # Ejecuta el API Gateway en el puerto 5000
    app.run(port=5000)
