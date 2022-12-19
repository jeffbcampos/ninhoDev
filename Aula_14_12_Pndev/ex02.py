#class calculadora com loop infinito que substitui o ultimo valor colocando o novo valor com operadores nas opções

class Calculadora:
    def __init__(self, valor):
        self.valor = valor

    def soma(self, valor):
        self.valor += valor

    def subtracao(self, valor):
        self.valor -= valor

    def multiplicacao(self, valor):
        self.valor *= valor

    def divisao(self, valor):
        self.valor /= valor

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def limpar(self):
        self.valor = 0

    def __str__(self):
        return f'Valor: {self.valor}'

primeiroValor = float(input('Digite o primeiro valor: '))
calc = Calculadora(primeiroValor)

while True:
    print('''
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Limpar
    6 - Sair
    ''')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        valor = float(input('Digite o valor a ser somado: '))
        calc.soma(valor)
        print(calc)
    elif opcao == 2:
        valor = float(input('Digite o valor a ser subtraído: '))
        calc.subtracao(valor)
        print(calc)
    elif opcao == 3:
        valor = float(input('Digite o valor a ser multiplicado: '))
        calc.multiplicacao(valor)
        print(calc)
    elif opcao == 4:
        valor = float(input('Digite o valor a ser dividido: '))
        calc.divisao(valor)
        print(calc)
    elif opcao == 5:
        calc.limpar()
        primeiroValor = float(input('Digite o primeiro valor: '))
        calc = Calculadora(primeiroValor)
        print(calc)
    elif opcao == 6:
        break
    else:
        print('Opção inválida!')

