import time 
import os
import csv

#Clase base que servira para la creacion de los objetos libros.

class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial,autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autores = autores

    def set_autores(self, autores):
        self.autores = autores

    def get_autores(self):
        return self.autores

    def get_genero(self):
        return self.genero

    def get_titulo(self):
        return self.titulo

    def get_isbn(self):
        return self.isbn

    def get_editorial(self):
        return self.editorial
        
    def mostrar_info(self):
        return f"({self.id})|{self.titulo} | {self.genero} | {self.isbn} | {self.editorial} | {self.get_autores()}"

    def __repr__(self):
        return f"({self.id})|{self.titulo} | {self.genero} | {self.isbn} | {self.editorial} | {self.get_autores()}"


#Metodos a realizar
# 1 Leer archivo(Jesus)
# 2 Listar libros(Jefferson)
# 3 Agregar libros(Jefferson)
# 4 Eliminar libros(Jefferson o Jesus)
# 5 Buscar Libro por ISBN o titulo (Jefferson o Jesus)
# 6 Ordenar libros por titulo (Jefferson o Jesus)
# 7 Buscar libros por autor, editorial, y/o genero (Jefferson o Jesus)
# 8 Buscar libros por numero de autores (Jefferson o Jesus)
# 9 Editar Libro (Jesus)
# 10 Guardar Libros(Jesus)

#FUNCIONES UTILES
def input_data_libro(msg=""):
    """
    :param msg: "Mensaje adicional que sera mostrado al momento de crear/editar
    """

    campos_libro = [
        "Ingrese un titulo : ", "ingrese un genero : ",
        "Digite el isbn : ", "ingrese una editorial : ",
        "Escriba los autores(si hay mas de uno use una ',') :"
    ]
    datos_obtenidos = []
    print(msg)
    for pregunta in campos_libro:
        dato = input(pregunta)
        datos_obtenidos.append(dato)
    return datos_obtenidos

#1 CARGAR ARCHIVO
def cargar_archivo(nombre_archivo:str):
    try:
        data_libros = []
        with open(nombre_archivo, encoding='utf-8') as archivo:
            data_archivo = csv.reader(archivo)
            for indice, data in enumerate(data_archivo):
                if indice != 0:
                    id, titulo, genero, isbn, editorial, autores = data
                    autores = autores.split('|')
                    libro_instancia = Libro(id, titulo, genero, isbn, editorial, autores)
                    data_libros.append(libro_instancia)
                else:
                    data_libros.append(data)            
            print('Datos cargados correctamente!')
            time.sleep(1)
    except FileNotFoundError:
        print("El archivo no existe.")        
        return nombre_archivo, data_libros
    return nombre_archivo,data_libros

#2 LISTAR LIBROS
def listar_libros(data:list):
    print(data[0])
    for libro_instancia in data[1::]:
        print(libro_instancia)


#3 AGREGAR (CREAR) LIBRO
def crear_libro(data:list) -> list:
    id = int(data[-1].id) + 1
    preguntas = [
        "Ingrese un titulo : ", "ingrese un genero : ",
        "Digite el isbn : ", "ingrese una editorial : ",
        "Escriba los autores(si hay mas de uno use una ',') :"
    ]
    respuestas = []
    for pregunta in preguntas:
        dato = input(pregunta)
        respuestas.append(dato)

    titulo, genero, isbn, editorial, autores = respuestas
    titulo = titulo.capitalize()
    autores = autores.split(',')

    libro_instancia  = Libro(id, titulo, genero, isbn, editorial, autores)
    data.append(libro_instancia)
    print(libro_instancia)
    print('Libro creado correctamente!')
    time.sleep(1)
    return data

#4 ELIMINAR LIBRO
def borrar_libro(data:list, id:int) -> list:
    print(data[0])
    for indice, item in enumerate(data[1::], start=1):
        if int(id) == int(item.id):
            libro = data.pop(indice)
            print(libro)
            print('El libro ha sido eliminado correctamente!')
            time.sleep(2)
    return data




#6 ORDENAR LIBROS POR TITULO
def ordenar_libros_por_titulo(data:list) -> list:
    #data[0] = headers
    print(data[0])
    instancias_libros = data[1::]
    instancias_libros.sort(key=lambda x: x.titulo, reverse=False)
    for item in instancias_libros:
        print(item)
    return data
#hay que definir las funciones de los tipos de busqueda
#__________________________________________________________

 


#__________________________________________________________________________________________

#10 GUARDAR DATOS 
def guardar_datos(datos_libros, nombre_archivo):
    with open(str(nombre_archivo), 'w') as archivo:
        print('ingreso al open')
        writer = csv.writer(archivo, delimiter=',')
        for indice, data in enumerate(datos_libros):
            print(str(indice)+ 'iterando for')
            
            if indice != 0:
                print([data.id, data.titulo, data.get_genero(), data.isbn, data.editorial, "|".join(data.autores)])
                writer.writerow([data.id, data.titulo, data.get_genero(), data.isbn, data.editorial, "|".join(data.autores)])
            else:
                writer.writerow(data)    
        print('Datos guardados exitosamente.')
    return "Datos guardados exitosamente."


menu_opciones = {
    1: 'Cargar Archivo',
    2: 'Listar Libros',
    3: 'Agregar libro',
    4: 'Eliminar libro',
    5: 'Buscar Libro por ISBN o titulo',
    6: 'Ordenar libros por titulo',
    7: 'Buscar libros por autor, editorial, y/o genero',
    8: 'Buscar libros por numero de autores',
    9: 'Editar Libro',
    10: 'Guardar libros en un nuevo archivo',
    11: 'Salir'
}

def mostrar_menu(opciones_del_menu):
    for key in opciones_del_menu.keys():
        print(str(key)+'-'+opciones_del_menu[key])
        
def verificar_datos(data):
    if not data:
        print('No tiene datos, cargue o cree un nuevo archivo.')
        time.sleep(2)
        return False
    return True
def mostrar_menu(opciones_del_menu):
    for key in opciones_del_menu.keys():
        print(str(key)+'-'+opciones_del_menu[key])


#FUNCIONES PARA INTERACTUAR CON EL MENU
def salir_al_menu_principal():
    respuesta = input('escriba "q" para regresar al menu principal : ')
    while respuesta.lower() not in ['q']:
        respuesta = input(
            'Por favor esriba "q" para salir al menu principal: ')
        respuesta = respuesta.lower()
    if respuesta == 'q':
        time.sleep(0.5)
        return True
    return False

#FUNCION QUE VERIFICA Y HAY DATOS CARGADOS O NO
def verificar_datos(data):
    if not data:
        time.sleep(1)
        return False
    return True



if  __name__ == '__main__':
    datos_libros = []
    nombre_archivo =  ''
    while True:
        print(' ======================')
        print('|   MENU PRINCIPAL     |')
        print(' ======================')
        mostrar_menu(menu_opciones)        
        opcion = ''
        try:
            opcion = int(input('Ingrese una accion a realizar: '))
            while opcion not in menu_opciones.keys():
                opcion = int(input(
                    'Por favor ingrese una opcion correcta.'))
        except:
            print('Por favor escoga un numero como accion a realizar')

        if opcion == 1:
            nombre_archivo = input('Ingrese el nombre del archivo: ')
            while len(nombre_archivo) == 0:
                nombre_archiv1o = input('Ingrese el nombre del archivo por favor. ')
            nombre_archivo +='.csv'
            nombre_archivo, datos_libros = cargar_archivo(nombre_archivo)
        
        if verificar_datos(datos_libros):
            if opcion == 2:
                print('Listar libros')
                pass
            elif opcion == 3:
                print('Agregar libro')
                pass
            elif opcion == 4:
                print('Eliminar libro')
                pass
            elif opcion == 5:
                print('Buscar libros por isbn o titulo')
                pass
            elif opcion == 6:
                print('ordenar libros por titulo')
                ordenar_libros_por_titulo(datos_libros)
                salir_al_menu_principal()                
            elif opcion == 7:
                print('Buscar libros por autor, editorial y/o genero')
                pass
            elif opcion == 8:
                print('Buscar libros por numero de autores')
                pass
            elif opcion == 9:
                print('Editar libro')
                pass    
            elif opcion == 10:
                print('Guardar libros en un nuevo archivo')
                nombre_nuevo_archivo = input('Escriba el nombre del nuevo archivo: ')
                nombre_nuevo_archivo += '.csv'
                if nombre_nuevo_archivo.lower() == nombre_archivo:
                    opcion = input('Desea sobreescribir el archivo? escriba si / no : ')
                    if opcion == 'si':
                        guardar_datos(datos_libros, nombre_archivo)
                    else:
                        print('No se ha podido guardar el archivo. Intente nuevamente')
                else:
                    print('what')
                    guardar_datos(datos_libros, nombre_nuevo_archivo)            
        elif opcion == 11:            
            exit()            
        else:
            print('Por favor escoga una opcion de las listadas.')
