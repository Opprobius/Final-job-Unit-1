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

    def mostrar_info(self):
        return f"({self.id})|{self.titulo} | {self.genero} | {self.isbn} | {self.editorial} | {self.get_autores()}"

    def __repr__(self):
        return f"({self.id})|{self.titulo} | {self.genero} | {self.isbn} | {self.editorial} | {self.get_autores()}"


#Metodos a realizar
# 1 Leer archivo(Jesus)
# 2 Listar libros
# 3 Agregar libros
# 4 Eliminar libros
# 5 Buscar Libro por ISBN o titulo
# 6 Ordenar libros por titulo
# 7 Buscar libros por autor, editorial, y/o genero
# 8 Buscar libros por numero de autores
# 9 Editar Libro
# 10 Guardar Libros

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
            time.sleep(2)
    except FileNotFoundError:
        print("El archivo no existe.")        
        return nombre_archivo, data_libros
    return nombre_archivo,data_libros


_, data = cargar_archivo('libros.csv')
print(data)