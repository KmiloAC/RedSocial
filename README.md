# RedSocial

Comandos de instalación

sudo apt update
sudo apt install python3-pip

ACTIVAR ENTORNO VIRTUAL

python3 -m venv myenv
source myenv/bin/activate
pip install flask


PARA PODER HACER PETICIONES HTTP
pip install requests

curl -X POST http://localhost:5001/usuarios -H "Content-Type: application/json" -d '{"nombre": "Carlos"}'
curl -X GET http://localhost:5000/usuarios

