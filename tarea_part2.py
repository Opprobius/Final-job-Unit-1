import requests
#https://pokeapi.co/api/v2
#Rutas para obtener la informacion

#Obtener todas las  generaciones
#https://pokeapi.co/api/v2/generation/
#Obtener pokemones por generacion
##https://pokeapi.co/api/v2/generation/{id or nombre_generacion}/

#Obtener todas las formas de pokemones
#https://pokeapi.co/api/v2/pokemon-shape/
#Obtener los pokemones por la forma seleccionada
#https://pokeapi.co/api/v2/pokemon-shape/{id or nombre_forma}/




#Obtener todas las habilidades
#https://pokeapi.co/api/v2/ability/?offset=20&limit=328
#Listar pokemones por habilidad
#https://pokeapi.co/api/v2/ability/{id or nombre_habilidad}/


#Obtener todos los habitats
#https://pokeapi.co/api/v2/pokemon-habitat/
#Listar pokemones por habitat seleccionado
#https://pokeapi.co/api/v2/pokemon-habitat/{id or nombre_habitat}/


#1- LISTAR POKEMONES POR GENERACION //1era Pregunta
def listar_generaciones_de_pokemon():
    generaciones = ''
    peticion = requests.get('https://pokeapi.co/api/v2/generation/')
    if peticion.status_code == 200:
        peticion = peticion.json()
        for indice, datos in enumerate(peticion['results'], start=1):
            generaciones += f"{indice}.- {datos['name']}\n"
        print(generaciones)
        
def listar_pokemones_por_generacion(generacion):
    peticion = requests.get(f"https://pokeapi.co/api/v2/generation/{generacion}/")
    resultado = ''
    if peticion.status_code == 200:
        print(' =================================')
        print(f"| POKEMONES DE LA GENERACION {generacion}   |")
        print(' =================================')
        peticion = peticion.json()
        for indice, pokemon in enumerate(peticion['pokemon_species'], start=1):
            if indice%7 == 0:
                resultado += f"| {pokemon['name']}\t\n"
            else:
                resultado += f"| {pokemon['name']}\t"
        print(resultado)
        return ""
    else:
        print('Aun no existe esa generacion ')
        return ""


#2 LISTAR POKEMONES POR FORMA // 2da pregunta
def obtener_forma_de_pokemones():
    forma_pokemones= ''
    peticion = requests.get('https://pokeapi.co/api/v2/pokemon-shape/')
    if peticion.status_code == 200:
        peticion = peticion.json()
        for indice,datos in enumerate(peticion['results'], start=1):
            if indice % 5 == 0:
                forma_pokemones += f"| {indice}.- {datos['name']}\t\n"
            else:
                forma_pokemones += f"|{indice}.- {datos['name']}\t"
        print(forma_pokemones)
    else:
        print('Algo ha ocurrido en el servidor, intente más tarde.')
        return forma_pokemones

def obtener_pokemones_por_forma(forma):
    pokemones = ''
    peticion = requests.get(f"https://pokeapi.co/api/v2/pokemon-shape/{forma}")
    if peticion.status_code == 200:
        peticion = peticion.json()
        print(' =================================')
        print(f"| POKEMONES DE forma {peticion['name']}   |")
        print(' =================================')
        for indice, datos in enumerate(peticion['pokemon_species']):
            if indice %5==0:
                pokemones += f"| {datos['name']}\t\n"
            else:
                pokemones += f"| {datos['name']}\t"
        print(pokemones)
        return pokemones
    else:
        print('Algo ha ocurrido en el servidor')
        return ""


#3 LISTAR POKEMONES POR HABILIDAD // tercera pregunta
def obtener_habilidades_de_pokemones():
    habilidad_pokemones = ''
    peticion = requests.get('https://pokeapi.co/api/v2/ability/?offset=20&limit=327')
    if peticion.status_code == 200:
        peticion = peticion.json()
        for indice,datos in enumerate(peticion['results'], start=1):
            if indice % 8 == 0:
                habilidad_pokemones += f"| {''.join(filter(str.isdigit, datos['url']))[1::]}.- {datos['name']}\t\n"
            else:
                habilidad_pokemones += f"|{''.join(filter(str.isdigit, datos['url']))[1::]}.- {datos['name']}\t"
        print(habilidad_pokemones)
    else:
        print('Algo ha ocurrido en el servidor, intente más tarde.')
        return habilidad_pokemones
        
def obtener_pokemones_con_habilidad(habilidad):
    print(habilidad)
    pokemones = ''
    peticion = requests.get(f"https://pokeapi.co/api/v2/ability/{habilidad}/")
    if peticion.status_code == 200:
        peticion = peticion.json()
        print(' =================================')
        print(f"| POKEMONES CON habilidad {peticion['name']}   |")
        print(' =================================')
        for indice, pokemon in enumerate(peticion['pokemon'], start=1):
            if indice %3 == 0:
                pokemones += '|'+pokemon['pokemon']['name']+'\n'
            else:
                pokemones += '|'+pokemon['pokemon']['name']+'|\t'
        if len(pokemones) > 0:
            print(pokemones)
        else:
            print('Aun no hay pokemones que tengan esa habilidad.')
    else:
        print("La habilidad no existe y/o ha ocurrido algo en el servidor")
        return "La habilidad no existe y/o ha ocurrido algo en el servidor"
    return ""
#4ta pregunta
def obtener_habitat_de_pokemones():
    habitat_pokemones = ''
    peticion = requests.get('https://pokeapi.co/api/v2/pokemon-habitat/')
    if peticion.status_code == 200:
        peticion = peticion.json()
        for indice,datos in enumerate(peticion['results'], start=1):
            if indice % 5 == 0:
                habitat_pokemones += f"| {indice}.- {datos['name']}\t\n"
            else:
                habitat_pokemones += f"|{indice}.- {datos['name']}\t"
        print(habitat_pokemones)
    else:
        print('Algo ha ocurrido en el servidor')

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

#FUNCION QUE VERIFICA EL INPUT QUE HA INGRESADO EL USUARIO
def opcion_escogida_int_cadena(msg=None):
    entrada = ''
    try:
        if msg != None:
            print(msg)
        entrada = input('Elija una opcion:  ')
        if entrada == int or entrada == str:
            pass
    except:
        print('Porfavor escoja una opcion de la lista')
    return entrada



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
            listar_generaciones_de_pokemon()
            opcion_escogida = opcion_escogida_int_cadena(msg='Escribe el numero de la generacion que quieres.')
            listar_pokemones_por_generacion(opcion_escogida)
        elif opcion == 2:
            obtener_forma_de_pokemones()
            opcion_escogida = opcion_escogida_int_cadena(msg='Cual forma de pokemon desea buscar?')
            obtener_pokemones_por_forma(opcion_escogida)
        elif opcion == 3:
            obtener_habilidades_de_pokemones()
            print('Para listar los pokemones debe')
            opcion_escogida = opcion_escogida_int_cadena(msg='escribir el numero y/o nombre de la habilidad')
            obtener_pokemones_con_habilidad(opcion_escogida)
        elif opcion == 4:
            print('Listar pokemones por habitat')
        elif opcion == 5:
            print('Listar pokemones por tipo')
        elif opcion == 6:
            exit()
        else:
            print('Por favor ingrese una opcion correcta.')

    




