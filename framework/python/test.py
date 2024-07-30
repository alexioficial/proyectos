import requests

url = "http://localhost:5000/test/hola"  # Asegúrate de que la URL sea correcta

data = {
    'nombre': 'asdf',
    'apellido': '4'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Solicitud exitosa:")
    print(response.text)
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
