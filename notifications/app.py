from flask import Flask, request, jsonify
import threading
import time

# Configuración e inicialización del microservicio de notificaciones
app = Flask(__name__)

# Validaciones y Configuración Básica
def validar_datos(data):
    # Ejemplo de validación para asegurar que todos los campos necesarios están presentes
    required_fields = ["user_id", "notification_type", "message"]
    for field in required_fields:
        if field not in data:
            return False, f"El campo {field} es obligatorio."
    return True, "Validación exitosa."

# Gestión de Notificaciones en Hilos
def enviar_notificacion(user_id, notification_type, message):
    # Esta función simula el envío de una notificación con hilos
    time.sleep(2)  # Simula la latencia de envío de la notificación
    print(f"Notificación enviada a usuario {user_id}: {message} (Tipo: {notification_type})")

@app.route('/notifications/send', methods=['POST'])
def enviar_notificacion_endpoint():
    data = request.get_json()

    # Validación de los datos de la notificación
    is_valid, msg = validar_datos(data)
    if not is_valid:
        return jsonify({"error": msg}), 400

    user_id = data["user_id"]
    notification_type = data["notification_type"]
    message = data["message"]

    # Crear un hilo para enviar la notificación de forma concurrente
    notificacion_thread = threading.Thread(target=enviar_notificacion, args=(user_id, notification_type, message))
    notificacion_thread.start()

    return jsonify({"status": "Enviando notificación en segundo plano."}), 202

# Funcionalidades Adicionales de Notificación
@app.route('/notifications/history/<user_id>', methods=['GET'])
def obtener_historial_notificaciones(user_id):
    # Simula la recuperación de un historial de notificaciones
    historial = [
        {"notification_type": "info", "message": "Bienvenido a la plataforma."},
        {"notification_type": "alert", "message": "Tu suscripción está por vencer."},
        {"notification_type": "reminder", "message": "Tienes 3 nuevas publicaciones sin leer."}
    ]
    return jsonify({"user_id": user_id, "history": historial}), 200

@app.route('/notifications/settings/<user_id>', methods=['GET', 'POST'])
def gestionar_configuracion_notificaciones(user_id):
    if request.method == 'POST':
        data = request.get_json()
        # Simula el guardado de configuración de notificaciones
        print(f"Configuración de notificaciones para usuario {user_id}: {data}")
        return jsonify({"status": "Configuración guardada exitosamente."}), 201
    else:
        # Simula la recuperación de configuración de notificaciones
        configuracion = {"email_notifications": True, "sms_notifications": False}
        return jsonify({"user_id": user_id, "settings": configuracion}), 200

# Punto de entrada para pruebas unitarias del microservicio de notificaciones
if __name__ == '__main__':
    app.run(port=5002, debug=True)