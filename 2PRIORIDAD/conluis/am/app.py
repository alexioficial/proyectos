from flask_session import Session
from flask import Flask
from uuid import uuid4

app = Flask(__name__)

llave = uuid4().hex
app.config.from_mapping(
    SECRET_KEY = llave,
    SESSION_PERMANENT = True,
    SESSION_TYPE = 'filesystem'
)
Session(app)

from routes.RInicio import bp as Inicio
from routes.RAuth import bp as Auth
from routes.RHome import bp as Home

app.register_blueprint(Inicio)
app.register_blueprint(Auth)
app.register_blueprint(Home)

if __name__ == '__main__':
    app.run('0.0.0.0', 7101, True, True)