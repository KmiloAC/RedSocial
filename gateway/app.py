# gateway/app.py
from flask import Flask
from routes import gateway  # Importa el Blueprint desde routes.py

app = Flask(__name__)

# Registra el Blueprint en la aplicación
app.register_blueprint(gateway)

if __name__ == '__main__':
    app.run(port=5000)
