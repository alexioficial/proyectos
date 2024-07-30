from flask import Blueprint, render_template, redirect, request, session
import components.tools as tools
import db.DBuser as db

bp = Blueprint('Auth', __name__)

@bp.route('/Login', methods = ['GET', 'POST'])
def Login():
    if 'iduser' in session:
        return redirect('/Home')
    else:
        if request.method == 'POST':
            try:
                data = request.get_json()
                username = data.get('username')
                password = tools.Encode(data.get('password'))
                login = db.Login()
                if login == None:
                    return {'estatus': 1, 'msj': 'Usuario o contraseña incorrectos'}
                else:
                    session['user'] = login
                    session['iduser'] = login['iduser']
                    return {'estatus': 0, 'redirect': '/Home'}
            except Exception as e:
                return tools.Err(e)
        return render_template('auth/Login.html')

@bp.route('/Logout', methods = ['POST'])
def Logout():
    try:
        session.pop('user', None)
        session.pop('iduser', None)
        return {'estatus': 0, 'redirect': '/'}
    except Exception as e:
        print(str(e))
        return tools.Err(e)