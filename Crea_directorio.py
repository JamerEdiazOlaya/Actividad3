import os

def create_directory(path):
    try:
        os.mkdir(path)
        return {'status': 'OK', 'message': 'Directorio creado exitosamente'}
    except OSError:
        return {'status': 'Error', 'message': 'No se pudo crear el directorio'}
