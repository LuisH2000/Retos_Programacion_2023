import requests

# URL de la API
url = 'https://pokeapi.co/api/v2/pokemon/'
pokemon = input("Ingresar el nombre de un pokemon o su id: ")
url += pokemon

# Realiza una solicitud GET
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Procesa la respuesta JSON
    data = response.json()
    print(f"Nombre: {data["name"]}")
    print(f"Id: {data["id"]}")
    print(f"Peso: {data["weight"]}")
    print(f"Altura: {data["height"]}")
    types = ""
    for type in data['types']:
        types += type["type"]["name"] + ", "
    print(f"Tipos: {types[:-2]}") 
else:
    print(f'Error en la solicitud: {response.status_code}')

'''

#--------------------------------------------------------------------
# URL de la API
url = 'https://api.ejemplo.com/data'

# Encabezados con token de autenticación
headers = {
    'Authorization': 'Bearer tu_token_aqui'
}

# Realiza una solicitud GET con autenticación
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error en la solicitud: {response.status_code}')
#--------------------------------------------------------------------
# URL de la API
url = 'https://api.ejemplo.com/create'

# Datos a enviar
data = {
    'nombre': 'John',
    'edad': 30
}

# Realiza una solicitud POST
response = requests.post(url, json=data)

if response.status_code == 201:
    print('Recurso creado exitosamente')
else:
    print(f'Error: {response.status_code}')
'''