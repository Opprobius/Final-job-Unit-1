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


#pokemon-habitat
#type

#1- LISTAR POKEMONES POR GENERACION
def listar_generaciones_de_pokemon():
    generaciones = ''
    peticion = requests.get('https://pokeapi.co/api/v2/generation/')
    if peticion.status_code == 200:
        peticion = peticion.json()
        for indice, datos in enumerate(peticion['results'], start=1):
            generaciones += f"{indice}.- {datos['name']}\n"
        print(generaciones)
        
def listar_pokemones_por_generacion():
    pokemones_por_generacion = ''
    peticion = requests.get(f"https://pokeapi.co/api/v2/generation/{generacion}/")
    if peticion.status_code == 200:        
        peticion = peticion.json()
        print(' =================================')
        print(f"| POKEMONES DE LA GENERACION {peticion['name']}   |")
        print(' =================================')
        for indice, pokemon in enumerate(peticion['pokemon_species'], start=1):
            if indice%7 == 0:
                resultado += f"| {pokemon['name']}\t\n"
            else:
                resultado += f"| {pokemon['name']}\t"
        print(resultado)
        return ""
    else:
        print('Aun no existe esa generacion y/o algo ha ocurrido en el servidor.')
        return ""


#2 LISTAR POKEMONES POR FORMA
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


#3 LISTAR POKEMONES POR HABILIDAD


def obtener_habilidades_de_pokemones():
    pass
        


def obtener_pokemones_con_habilidad(habilidad):
    pass



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

    




