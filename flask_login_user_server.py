from flask import Flask, request, jsonify

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

if __name__ == '__main__':
    app.run(host='127.0.0.0', port=8000)

