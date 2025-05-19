class Livro:
    def __init__(self,titulo,autor,isbn,disponivel=True):
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.disponivel=disponivel

class Usuario:
    def __init__(self,nome,ID,livros_emprestados):
        self.nome=nome
        self.ID=ID
        self.livros_emprestados=livros_emprestados

class Biblioteca:
    def __init__(self, livros, usuarios):
        self.livros= livros
        self.usuarios= usuarios

    def emprestar_livro(self, idUsario, isbnLivro):
        for usuario in self.usuarios:
            if usuario.ID == idUsario:
                for livro in self.livros:
                    if (livro.isbn == isbnLivro) and (livro.disponivel == True):                        
                        print(f"O livro {livro.titulo} foi emprestado para o usuario {usuario.nome}")

livro1= Livro("mOBYDICK","robson",3456,False)
livro2= Livro("Harry Potter","Simao",8888,True)
livro3= Livro("Senhor do Python","Pedro",555,True)

lista_livros = []
lista_livros.append(livro1)
lista_livros.append(livro2)
lista_livros.append(livro3)

usuario1=Usuario("leo",1,[])
usuario2=Usuario("maria",2,[])
usuario3=Usuario("joao",3,[])

lista_usuarios = []
lista_usuarios.append(usuario1)
lista_usuarios.append(usuario2)
lista_usuarios.append(usuario3)


bibi=Biblioteca(lista_livros, lista_usuarios)

bibi.emprestar_livro(3, 8888)