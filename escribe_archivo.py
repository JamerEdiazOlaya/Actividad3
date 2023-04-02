def write_file(path, content):
    try:
        with open(path, 'w') as file:
            file.write(content)
        return {'status': 'OK', 'message': 'Archivo escrito exitosamente'}
    except IsADirectoryError:
        return {'status': 'Error', 'message': 'El path corresponde a un directorio, no a un archivo'}
