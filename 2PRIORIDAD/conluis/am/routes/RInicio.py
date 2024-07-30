from flask import Blueprint, session, redirect, render_template
from functools import wraps

bp = Blueprint('Inicio', __name__)

def login_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        if 'user' not in session:
            return redirect('/Login')
        return f(*args, **kwargs)
    return decorador

@bp.route('/', methods = ['GET'])
def index():
    try:
        print(session.get('user'))
        return redirect('/Home')
    except Exception:
        return redirect('/Login')