from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ruta para crear un nuevo directorio
@app.route('/directory', methods=['POST'])
def create_directory():
    directory_name = request.json.get('directory_name')
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        return jsonify({'status': 'OK', 'message': 'Directorio creado exitosamente'})
    else:
        return jsonify({'status': 'Error', 'message': 'El directorio ya existe'})

# Ruta para crear un nuevo archivo
@app.route('/file', methods=['POST'])
def create_file():
    file_name = request.json.get('file_name')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write('')
        return jsonify({'status': 'OK', 'message': 'Archivo creado exitosamente'})
    else:
        return jsonify({'status': 'Error', 'message': 'El archivo ya existe'})

# Ruta para leer el contenido de un archivo
@app.route('/file', methods=['GET'])
def read_file():
    file_name = request.args.get('file_name')
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            content = f.read()
        return jsonify({'status': 'OK', 'content': content})
    else:
        return jsonify({'status': 'Error', 'message': 'El archivo no existe'})

# Ruta para actualizar el contenido de un archivo
@app.route('/file', methods=['PUT'])
def update_file():
    file_name = request.json.get('file_name')
    content = request.json.get('content')
    if os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write(content)
        return jsonify({'status': 'OK', 'message': 'Archivo actualizado exitosamente'})
    else:
        return jsonify({'status': 'Error', 'message': 'El archivo no existe'})

# Ruta para eliminar un archivo o directorio
@app.route('/path', methods=['DELETE'])
def delete_path():
    path = request.json.get('path')
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            return jsonify({'status': 'OK', 'message': 'Archivo eliminado exitosamente'})
        elif os.path.isdir(path):
            os.rmdir(path)
            return jsonify({'status': 'OK', 'message': 'Directorio eliminado exitosamente'})
    else:
        return jsonify({'status': 'Error', 'message': 'El archivo o directorio no existe'})

if __name__ == '__main__':
    app.run()
