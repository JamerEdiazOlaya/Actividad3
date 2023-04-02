def update_file(path, content):
    try:
        with open(path, 'a') as file:
            file.write(content)
        return {'status': 'OK', 'message': 'Archivo actualizado exitosamente'}
    except FileNotFoundError:
        return {'status': 'Error', 'message': 'El archivo no existe'}
    except IsADirectoryError:
        return {'status': 'Error', 'message': 'El path corresponde a un directorio, no a un archivo'}
