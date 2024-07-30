from flask import Blueprint, render_template, jsonify, session, request
from routes.RInicio import login_requerido
from db.DBUsuarios import usuario
import components.tools as tools
import db.DBUsuarios as dbuser
import base64

bp = Blueprint('Home', __name__)

generos = {
    'f': '<span class="fa-solid fa-venus c-pointer" style="color: #ff00ff;"></span>',
    'm': '<span class="fa-solid fa-mars c-pointer" style="color: #0000ff;"></span>',
    'NA': '<span class="fa-solid fa-genderless c-pointer" style="color: gray;"></span>'
}

@bp.route('/Home')
@login_requerido
def Home():
    iduser = session.get('iduser')
    dtuser = dbuser.UserById(iduser)
    imagen = f'data:image/png;base64,{dtuser["img"]}' if dtuser['img'] != '' else '/static/img/usernf.png'
    html = f'''
        <div class="col-md-6">
            <center>
                <img src="{imagen}" id="profile-img" class="profile">
                <input type="file" class="d-none" id="profile-img-input" accept="image/*">
            </center>
        </div>
        <div class="col-md-6">
            <input value="{dtuser['username']}" id="username" class="profile p-input-fc">
            <div class="form-group mt-3">
                <label for="password">Password</label>
                <div class="input-group">
                    <button class="btn" id="show-pass">
                        <span class="fa-solid fa-eye"></span>
                    </button>
                    <input type="password" class="form-control profile" id="password" value="{dtuser['password']}">
                </div>
            </div>
        </div>
        <center>
            <label class="mt-2">Sobre mi</label>
            <textarea class="profile p-input-fc" spellcheck="false" id="biografia">{dtuser['biografia']}</textarea>
        </center>
    '''
    genero = generos.get(dtuser['genero'])
    return render_template('Home.html', iduser = iduser, html = html, genero = genero)

@bp.post('/UpdateGender')
def UpdateGender():
    try:
        iduser = session.get('iduser')
        genero = dbuser.UserById(iduser)['genero']
        gender_next = {
            'f': 'm',
            'm': 'NA',
            'NA': 'f'
        }
        genero_siguiente = gender_next.get(genero)
        usuario.update_one({'iduser': iduser}, {'$set': {'genero': genero_siguiente}})
        return {'estatus': 0, 'html': generos.get(genero_siguiente)}
    except Exception as e:
        return tools.Err(e)

@bp.post('/UpdateImg')
def UpdateImg():
    try:
        archivo = request.files.get('archivo')
        iduser = session.get('iduser')

        if archivo and iduser:
            # Leer el contenido del archivo en bytes
            img_bytes = archivo.read()
            # Convertir los bytes en una cadena Base64
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            dbuser.UpdateImg(iduser, img_base64)

            return jsonify({'estatus': 0, 'img': f'data:image/png;base64,{img_base64}'})
        else:
            return jsonify({'estatus': 2})
    except Exception as e:
        return jsonify({'estatus': 1, 'msj': str(e)})

@bp.post('/UpdateUser/<info>')
def UpdateUser(info):
    try:
        data = request.get_json()
        value = data.get('value')
        iduser = session.get('iduser')
        usuario.update_one({'iduser': iduser}, {'$set': {info: value}})
        return {'estatus': 0}
    except Exception as e:
        return tools.Err(e)

@bp.post('/GetNotifications')
def GetNotifications():
    try:
        iduser = session.get('iduser')
        notificaciones = dbuser.UserById(iduser)['notificaciones']
        html = ''
        for n in notificaciones:
            tipo = n['tipo']
            if n['estatus'] == 1:
                if tipo == 'friend':
                    username = dbuser.UserById(n['iduser'])['username']
                    html += f'''
                        <div class="micard friend mt-3">
                            <h4 id="{iduser}__{n['idnotify']}">{username}</h4>
                            <hr>
                            <p>{n['msj']}</p>
                            <div class="row">
                                <div class="col-md-6">
                                    <button class="accept-btn btn btn-success w-100" onclick="AcceptFriend('{n['iduser']}', '{iduser}__{n['idnotify']}')">Aceptar</button>
                                </div>
                                <div class="col-md-6">
                                    <button class="deny-btn btn btn-danger w-100" onclick="DeleteNofify('{iduser}__{n['idnotify']}');">Denegar</button>
                                </div>
                            </div>
                        </div>
                    '''
                if tipo == 'msj':
                    username = dbuser.UserById(n['iduser'])['username']
                    html += f'''
                        <div class="micard msj mt-3">
                            <h4 id="{iduser}__{n['idnotify']}">
                                {username}
                                <span class="btn btn-danger fa fa-trash" onclick="DeleteNofify('{iduser}__{n['idnotify']}');"></span>
                            </h4>
                            <hr>
                            <p>{n['msj']}</p>
                        </div>
                    '''
                if tipo == 'update':
                    cosas = ''
                    for c in n['cosas']:
                        cosas += f'''
                            <li>{c}</li>
                        '''
                    html += f'''
                        <div class="micard update mt-3">
                            <h4 id="{iduser}__{n['idnotify']}">
                                Actualizacion
                                <span class="btn btn-danger fa fa-trash" onclick="DeleteNofify('{iduser}__{n['idnotify']}');"></span>
                            </h4>
                            <hr>
                            <p>{n['msj']}</p>
                            <ul>{cosas}</ul>
                        </div>
                    '''
        return {'estatus': 0, 'html': f'<center>{html}</center>'}
    except Exception as e:
        return tools.Err(e)

@bp.post('/DeleteNotify')
def DeleteNotify():
    try:
        data = request.get_json()
        iduser = data.get('iduser')
        idnotify = data.get('idnotify')

        usuario.update_one(
            {'iduser': iduser, 'notificaciones.idnotify': idnotify},
            {'$set': {'notificaciones.$.estatus': 0}}
        )
        return {'estatus': 0}
    except Exception as e:
        return tools.Err(e)

@bp.post('/AcceptFriend')
def AcceptFriend():
    try:
        data = request.get_json()
        iduser = session.get('iduser')
        idfriend = data.get('idfriend')

        dbuser.AcceptFriend(iduser, idfriend)
        dbuser.AcceptFriend(idfriend, iduser)
        return {'estatus': 0}
    except Exception as e:
        return tools.Err(e)

@bp.post('/GetContacts')
def GetContacts():
    try:
        iduser = session.get('iduser')
        contactos = dbuser.UserById(iduser)['contactos']
        html = ''
        for c in contactos:
            dtuser = dbuser.UserById(c['iduser'])
            imagen = f'data:image/png;base64,{dtuser["img"]}' if dtuser['img'] != '' else '/static/img/usernf.png'
            html += f'''
                <div class="micard mt-3 p-2 row">
                    <div class="col-md-4">
                        <img src="{imagen}" style="border-radius: 100000px" width="100" height="100">
                    </div>
                    <div class="col-md-8">
                        <h4><a href="/Chat/{c['idcontact']}" class="profile">{c['as']}</a></h4>
                        <hr>
                        <p class="msj">{dtuser['biografia']}</p>
                    </div>
                </div>
            '''
        return {'estatus': 0, 'html': f'<center>{html}</center>'}
    except Exception as e:
        return tools.Err(e)