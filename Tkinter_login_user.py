from tkinter import *
import requests

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Realizar una petición al servidor para autenticar al usuario
    response = requests.post('http://localhost:5000/login', json={'username': username, 'password': password})
    
    if response.json()['status'] == 'OK':
        # Si la autenticación es exitosa, mostrar un mensaje de bienvenida
        message_label.config(text='¡Bienvenido, {}!'.format(username))
    else:
        # Si la autenticación falla, mostrar un mensaje de error
        message_label.config(text='Error: {}'.format(response.json()['message']))

# Crear la ventana principal
root = Tk()

# Crear los widgets de la interfaz de usuario
username_label = Label(root, text='Usuario:')
username_entry = Entry(root)
password_label = Label(root, text='Contraseña:')
password_entry = Entry(root, show='*')
login_button = Button(root, text='Iniciar sesión', command=login)
message_label = Label(root, text='')

# Posicionar los widgets en la ventana principal
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=1)
message_label.grid(row=3, column=0, columnspan=2)

# Iniciar el bucle principal de la aplicación
root.mainloop()
