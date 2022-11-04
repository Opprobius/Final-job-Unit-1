import requests

#https://pokeapi.co/api/v2
#generation
#pokemon-shape
#ability
#pokemon-habitat
#type

#funciones del menu
menu_options = {
        1: 'Listar pokemons por generación',
        2: 'Listar pokemons por forma',
        3: 'Listar pokemons por habilidad',
        4: 'Listar pokemons por habitat.',
        5: 'Listar pokemons por tipo',
        6: 'Salir del programa.'
}

#peticiones de Forma
def obtener_1():
    var_1 = ''
    peticion = requests.get('url')
    if peticion.status_code == 200:
        peticion = peticion.json()
        for i, datos in enumerate(peticion['results'], start=1):
        
def obtener_2():
    var_2 = ''
    peticion = requests.get('url')
    if peticion.status_code == 200:
        peticion = peticion.json()
def obtener_3():
    var_3= ''
    peticion = requests.get('url')
    if peticion.status_code == 200:
        peticion = peticion.json()
        
def obtener_4():
    var_4 = ''
    peticion = requests.get('url')
    if peticion.status_code == 200:
        peticion = peticion.json()
def obtener_5():
    var_5 = ''
    peticion = requests.get('url')
    if peticion.status_code == 200:
        peticion = peticion.json()
