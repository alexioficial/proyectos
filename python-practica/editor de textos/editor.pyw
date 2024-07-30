from tkinter import *
from tkinter import filedialog
from io import open

ruta = '' # La utilizare para guardar la ruta del archivo

def nuevo():
    global ruta
    mensaje.set('Nuevo archivo')
    ruta = ''
    texto.delete(1.0, 'end')
    root.title('Mi editor')

def abrir():
    global ruta
    mensaje.set('Abrir archivo')
    ruta = filedialog.askopenfilename(
        initialdir = '.',
        filetypes = (
            ('Todos los archivos', '*.*'),
            ('Archivos de texto', '*.txt')
        ),
        title = 'Abrir archivo'
    )
    if ruta != '':
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + ' - Mi editor')

def guardar():
    mensaje.set('Guardar archivo')
    if ruta != '':
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Archivo guardado correctamente')
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set('Guardar archivo como')
    fichero = filedialog.asksaveasfile(
        title = 'Guardar archivo',
        mode = 'w',
        defaultextension = ''
    )
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Archivo guardado correctamente')
    else:
        mensaje.set('Guardado cancelado')
        ruta = ''

# Configuracion del root
root = Tk()
root.title('Mi editor')

# Menu Superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Nuevo', command = nuevo)
filemenu.add_command(label = 'Abir', command = abrir)
filemenu.add_command(label = 'Guardar', command = guardar)
filemenu.add_command(label = 'Guardar como', command = guardar_como)
filemenu.add_separator()
filemenu.add_command(label = 'Salir', command = root.quit)
menubar.add_cascade(menu = filemenu, label = 'Archivo')

# Caja de texto central
texto = Text(root)
texto.pack(fill = 'both', expand = 1)
texto.config(bd = 0, padx = 6, pady = 4, font = ('Calibri', 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar = mensaje, justify = 'left')
monitor.pack(side = 'left')


root.config(menu = menubar)

# Bucle de la aplicacion
root.mainloop()