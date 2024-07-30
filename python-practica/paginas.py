import requests
import json
import os
import re

pagina = input('Pagina: ')

output_file = "temp_output.txt"
os.system(f'ping {pagina} > {output_file}')

with open(output_file, 'r') as file:
    output = file.read()

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip_match = re.search(ip_pattern, output)

if ip_match:
    ip_address = ip_match.group()
else:
    print("No se encontró una dirección IP en el resultado del ping")

os.remove(output_file)

resp = requests.get(f'https://ipinfo.io/{ip_address}')
print(json.loads(resp.content.decode()))