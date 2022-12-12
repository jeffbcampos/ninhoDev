class Livro:
    def __init__(self, titulo, autor, paginas, preco):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco
    
    def getPreco(self):
        return self.preco
    
    def setPreco(self, novoPreco):
        self.preco = novoPreco

livro1 = input('Digite o título do livro: ')
autor = input('Digite o autor do livro: ')
paginas = int(input('Digite o número de páginas do livro: '))
preco = float(input('Digite o preço do livro: '))
livro = Livro(livro1, autor, paginas, preco)

print(f'O preço do livro {livro.titulo} é {livro.getPreco():.2f}')


novoPreco = float(input('Digite o novo preço do livro: '))
livro.setPreco(novoPreco)

print(f'O novo preço do livro {livro.titulo} é {livro.getPreco():.2f}')



