# Entendendo POO

# Criando uma classe
class Livro():
    # Criando atributos da classe
    def __init__(self):
        self.titulo = 'O Monge e o Executivo'
        self.isbn = 9988888
        print('Construtor chamado para criar um objeto desta classe')

    # Criando métodos da classe
    def imprime(self):
        print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))
        
# Criando uma instância da classe Livro
Livro1 = Livro()

# Imprimindo os atributos da classe Livro
print(Livro1.titulo)
print(Livro1.isbn)

# Imprimindo o tipo do objeto Livro1
print(type(Livro1))

# Imprimindo o método imprime da classe Livro
Livro1.imprime()

# Criando a classe Livro com parâmetros
class Livro():
    # Criando atributos da classe
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto desta classe')

    # Criando métodos da classe
    def imprime(self, titulo, isbn):
        print('Este é o livro %s e ISBN %d' %(titulo, isbn))
        
# Criando uma instância da classe Livro
Livro1 = Livro('A menina que roubava livros', 77886611)

# Imprimindo os atributos da classe Livro
print(Livro1.titulo)
print(Livro1.isbn)

# Imprimindo o tipo do objeto Livro1
print(type(Livro1))

# Imprimindo o método imprime da classe Livro
Livro1.imprime('A menina que roubava livros', 77886611)

# Criando a classe Cachorro
class Cachorro():
    # Criando atributos da classe
    def __init__(self, raca):
        self.raca = raca
        print('Construtor chamado para criar um objeto desta classe')
        
# Criando uma instância da classe Cachorro
Rex = Cachorro(raca = 'Labrador')

# Criando uma instância da classe Cachorro
Golias = Cachorro(raca = 'Huskie')

# Imprimindo o atributo da classe Cachorro

print('A raça do meu cachorro é: %s' %(Rex.raca))
print('A raça do meu cachorro é: %s' %(Golias.raca))


