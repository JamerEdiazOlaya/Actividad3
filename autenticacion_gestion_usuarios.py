from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ruta para autenticar a los usuarios
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Verificar que el usuario y la contraseña sean válidos
    if username == 'usuario' and password == 'contraseña':
        return jsonify({'status': 'OK'})
    else:
        return jsonify({'status': 'Error', 'message': 'Usuario o contraseña inválidos'})

# Ruta para crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    # Obtener los datos del nuevo usuario
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Verificar que el usuario no exista previamente
    if os.path.isdir(username):
        return jsonify({'status': 'Error', 'message': 'El usuario ya existe'})
    
    # Crear la carpeta para el nuevo usuario y guardar su contraseña en un archivo
    os.mkdir(username)
    with open(os.path.join(username, 'password.txt'), 'w') as f:
        f.write(password)
    
    return jsonify({'status': 'OK', 'message': 'Usuario creado exitosamente'})

if __name__ == '__main__':
    app.run()
