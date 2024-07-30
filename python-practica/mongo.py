import requests as req

a = req.get('https://localhost:27017')
b = req.post('https://localhost:27017', {})

print(a, b)