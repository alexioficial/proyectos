from dotenv import load_dotenv
import jwt
import os

load_dotenv()

LOGIN_ENCODE = os.getenv("LOGIN_ENCODE")

def Encode(mensaje, key):
    token = jwt.jwt.JWT.encode(payload = {'msj': mensaje}, key = key, alg = 'HS256')
    return token

def Decode(token, key):
    try:
        decoded_payload = jwt.jwt.JWT.decode(message = token, key = key, algorithms = ['HS256'])
        mensaje = decoded_payload.get('msj')
        return mensaje
    except Exception as e:
        print(str(e))