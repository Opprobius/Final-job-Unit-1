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

#


def input_data_libro(msg=""):
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

def borrar_libro(data, id):
    print(data[0])
    for indice, item in enumerate(data[1::], start=1):
        if int(id) == int(item.id):
            libro = data.pop(indice)
            print(libro)
            print('El libro ha sido eliminado correctamente!')
            time.sleep(2)
    return data

def crear_libro(data) -> list:
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
    autores = autores.split(',')

    libro_instancia  = Libro(id, titulo, genero, isbn, editorial, autores)
    data.append(libro_instancia)
    print(libro_instancia)
    print('Libro creado correctamente!')
    time.sleep(1)
    return data

def listar_libros(data):
    print(data[0])
    for libro_instancia in data[1::]:
        print(libro_instancia)
        
def crear_nuevo_archivo():
    filename ='libros1.csv'
    file = open('nuevo_archivo_libros.csv','w')
    file.write('Id,Titulo,Genero,Isbn,Editorial,Autores'+os.linesep)
    file.close()
    data_libros = cargar_archivo(filename)
    return data_libros

        
def cargar_archivo(nombre_archivo):
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

def order_books_by_title(data):
    #data[0] = headers
    print(data[0])
    instancias_libros = data[1::]
    instancias_libros.sort(key=lambda x: x.titulo, reverse=False)
    for item in instancias_libros:
        print(item)
    return data
#hay que definir las funciones de los tipos de busqueda
#__________________________________________________________
def buscar_libro_por_autor_editorial_genero(data, input_autor=None, input_editorial=None, input_genero=None):
    resultado = data[0]

    if input_autor != None:
        for indice, item in enumerate(data[1::], start=1):
            if str(input_autor).strip() in item.get_autores():
                resultado.append(item)

    elif input_editorial != None:
        for indice, item in enumerate(data[1::], start=1):
            if str(input_editorial).lower().strip() == item.get_editorial().lower().strip():
                resultado.append(item)

    elif input_genero != None:
        for indice, item in enumerate(data[1::], start=1):
            if str(input_genero).lower().strip() == item.get_genero().lower().strip():
                resultado.append(item)

    if len(resultado) > 0:
        listar_libros(resultado)
    else:
        print('No se han encontrado coincidencias.')
    return data

def buscar_libro_por_numero_autores(data_libros):
    try:
        numero_autores = int(input('Por cuantos autores desea listar'))
    except:
        print('Tiene que ingresar un numero')

    resultado = [data_libros[0]]
    for data in data_libros[1::]:
        if len(data.autores) == numero_autores:
            resultado.append(data)
    listar_libros(resultado)


def buscar_libro_por_isbn_titulo(data: list, input_isbn=None, input_titulo=None)->list:
    print(data[0])
    resultado = []
    if input_isbn != None:
        for indice, item in enumerate(data[1::], start=1):
            if str(input_isbn).strip() == item.get_isbn().strip():
                resultado.append(item)

    elif input_titulo != None:
        for indice, item in enumerate(data[1::], start=1):
            print(input_titulo+'??'+item.get_titulo())
            if str(input_titulo).lower().strip() == item.get_titulo().lower().strip():
                resultado.append(item)


    if len(resultado) > 0:
        print(resultado[0])
    else:
        print('No se han encontrado coincidencias.')
    return data


#__________________________________________________________________________________________

def parse_data_libro(instance_book):
    data = []
    data.append(instance_book.id)
    data.append(instance_book.titulo)
    data.append(instance_book.get_genero())
    data.append(instance_book.isbn)
    data.append(instance_book.editorial)
    autores = "|".join(instance_book.autores)
    data.append(autores)
    return data

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

if  __name__ == '__main__':
    datos_libros = []
    nombre_archivo = ''
    while True:
        print(' ======================')
        print('|   MENU PRINCIPAL     |')
        print(' ======================')
        mostrar_menu(menu_options)
        try:
            opcion = int(input('Que desea hacer?: '))
        except:
            print('Por favor ingrese una opcion valida.')
        if opcion == 1:
            nombre_archivo = input('Ingrese el nombre del archivo: ')
            while len(nombre_archivo) == 0:
                nombre_archiv1o = input('Ingrese el nombre del archivo por favor')
            nombre_archivo +='.csv'
            nombre_archivo, datos_libros = cargar_archivo(nombre_archivo)
        elif opcion == 2:
            if not verificar_datos(datos_libros):
                time.sleep(1)
            else:
                listar_libros(datos_libros)
                respuesta = input('escriba "q" para regresar al menu principal : ')
                while respuesta.lower() not in ['q']:
                    respuesta = input(
                        'Por favor esriba "q" para salir al menu principal: ')
                    respuesta = respuesta.lower()
                if respuesta == 'q':
                    time.sleep(1)


        elif opcion == 3:
            datos_libros = crear_libro(datos_libros)
        elif opcion == 4:
            id_libro = ''
            try:
                id_libro = int(input('Escriba el id del libro a eliminar'))
            except:
                print('Se necesita un id(numero)')
            if id_libro > 0:
                datos_libros = borrar_libro(datos_libros, id_libro)
                listar_libros(datos_libros)
        elif opcion == 5:
            mostrar_menu({
                1: 'Buscar por ISBN',
                2: 'Buscar por Titulo',
                3: 'Volver al menu principal'
            })
            while(True):
                try:
                    opcion = int(input('Ingrese una opcion'))
                    while opcion not in [1,2,3]:
                        opcion = int(input(
                            'Por favor ingrese una opcion correcta.'))
                except:
                    print('Por favor escoga un numero como accion a realizar')
                if opcion == 1:
                    print('Buscar por isbn')
                    isbn = input('Digite el isbn: ')
                    buscar_libro_por_isbn_titulo(datos_libros, input_isbn=isbn)
                    break
                elif opcion == 2:
                    print('Buscar por titulo')
                    titulo= input('Escriba el titulo del libro a buscar: ')
                    buscar_libro_por_isbn_titulo(datos_libros, input_titulo=titulo)
                    break
                elif opcion == 3:
                    break
                else:
                    print('Escoga una opcion por favor')
        elif opcion == 6:
            order_books_by_title(datos_libros)

        elif opcion == 7:
            mostrar_menu({
                1: 'Buscar por autor',
                2: 'Buscar por editorial',
                3: 'Buscar por genero',
                4: 'Regresar al menu principal'
            })
            while (True):
                try:
                    opcion = int(input('Ingrese una opcion'))
                    while opcion not in [1, 2, 3,4]:
                        opcion = int(input(
                            'Por favor ingrese una opcion correcta.'))
                except:
                    print('Por favor escoga un numero como accion a realizar')
                if opcion == 1:
                    print('Buscar por isbn')
                    autor = input('Escriba el nombre del autor: ')
                    buscar_libro_por_autor_editorial_genero(datos_libros, input_autor=autor)
                    break
                elif opcion == 2:
                    print('Buscar por titulo')
                    editorial = input('Escriba la editorial del libro a buscar: ')
                    buscar_libro_por_autor_editorial_genero(datos_libros, input_editorial=editorial)
                    break
                elif opcion == 3:
                    genero = input('Escriba el genero del libro a buscar: ')
                    buscar_libro_por_autor_editorial_genero(datos_libros, input_genero=genero)
                    break
                elif opcion == 4:
                    break
                else:
                    print('Escoga una opcion por favor')

        elif opcion == 8:
            buscar_libro_por_numero_autores(datos_libros)
        elif opcion == 9:
            print("editar libro, insetar un id")
            id_libro = ''
            try:
                id_libro = int(input('Escriba el id del libro a editar'))
            except:
                print('Se necesita un id(numero)')
            editar_libro(datos_libros, id_libro)
        elif opcion == 10:
            respuesta = input('Escriba el nombre del nuevo archivo: ')
            respuesta +='.csv'
            if respuesta.lower() == nombre_archivo:
                opcion = input('Desea sobreescribir el archivo? escriba si / no : ')
                if opcion == 'si':
                    guardar(datos_libros, nombre_archivo)
                else:
                    print('No se ha podido guardar el archivo. Intente nuevamente')
            else:
                print('what')
                guardar(datos_libros, respuesta)
        elif opcion == 11:
            exit()
        else:
            print('Opcion invalida. Por favor elija un numero correcto.')
