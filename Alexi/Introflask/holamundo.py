from crypt import methods
from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector
app = Flask(__name__)

midb = mysql.connector.connect (
    host = '192.168.0.100',
    user = 'alexi',
    password = 'Alexi1234-',
    database = 'alexi',
)

cursor = midb.cursor(dictionary=True)

@app.route('/') # Esto es una ruta
def index():
    return 'hola mundo'

@app.route('/posts/<post_id>', methods=['GET', 'POST'])
def lili(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es otro metodo y no GET'

@app.route('/lala/<usuario>') # Lo que esta entre '<>' es una variable
def lala(usuario):
    return usuario

@app.route('/lele')
def lele():
    cursor.execute('SELECT * FROM alexi.Usuario;')
    usuarios = cursor.fetchall()

    return render_template('lele.html', usuarios = usuarios)

@app.route('/home/', methods = ['GET']) # Hace coneccion con la carpeta templates y busca el archivo
def home():
    return render_template('home.html', mensaje = 'que haces aca?')

@app.route('/crear', methods = ['GET', 'POST'])
def crear():
    if request.method == 'POST':
        username = request.form['username']

        sql = 'insert into Usuario (username) values (%s)'
        values = (username)
        cursor.execute(sql, values)
        midb.commit()

        return redirect(url_for('lele'))

    return render_template('crear.html')