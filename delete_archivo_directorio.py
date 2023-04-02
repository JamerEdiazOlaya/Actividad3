import os

def delete_file_or_directory(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
        return {'status': 'OK', 'message': 'Archivo/directorio eliminado exitosamente'}
    except FileNotFoundError:
        return {'status': 'Error', 'message': 'El archivo/directorio no existe'}
