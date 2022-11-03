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
