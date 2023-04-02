def read_file(path):
    try:
        with open(path, 'r') as file:
            content = file.read()
        return {'status': 'OK', 'content': content}
    except FileNotFoundError:
        return {'status': 'Error', 'message': 'El archivo no existe'}
    except IsADirectoryError:
        return {'status': 'Error', 'message': 'El path corresponde a un directorio, no a un archivo'}
