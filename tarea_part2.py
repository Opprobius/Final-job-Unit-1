import requests
#https://pokeapi.co/api/v2
#Rutas para obtener la informacion
#generation
#pokemon-shape
#ability
#pokemon-habitat
#type


#peticiones de Forma
def obtener_1():
    var_1 = ''
    peticion = requests.get('url')
    if peticion.status_code == 200:
        peticion = peticion.json()
        for i, datos in enumerate(peticion['results'], start=1):
            pass
        
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



#FUNCIONES DEL MENU
menu_opciones = {
        1: 'Listar pokemons por generación',
        2: 'Listar pokemons por forma',
        3: 'Listar pokemons por habilidad',
        4: 'Listar pokemons por habitat.',
        5: 'Listar pokemons por tipo',
        6: 'Salir del programa.'
}

def mostrar_menu(opciones_menu):
    for key in opciones_menu.keys():
        print(str(key)+'-'+opciones_menu[key])



if __name__ == '__main__':
    while True:
        print(' ======================')
        print('|   MENU PRINCIPAL     |')
        print(' ======================')
        mostrar_menu(menu_opciones)

        try:
            opcion = int(input('Por favor seleccione una opción.'))
        except:
            print('Por favor ingrese una opción numerica')
        if opcion == 1:
            print('Listar pokemones por generacion')
        elif opcion == 2:
            print('Listar pokemones por forma')
        elif opcion == 3:
            print('Listar pokemones por habilidades')
        elif opcion == 4:
            print('Listar pokemones por habitat')
        elif opcion == 5:
            print('Listar pokemones por tipo')
        elif opcion == 6:
            print('Listar pokemones por tipo')
        else:
            print('Por favor ingrese una opcion correcta.')

    




