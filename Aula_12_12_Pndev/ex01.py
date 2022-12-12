#Crie um programa que utilize uma função para comparar o tamanho de duas strings. Essa função vai receber as 2 strings e vai determinar qual das duas palavras é a maior e imprimir na tela

def comparaString(string1, string2):
    if len(string1) > len(string2):
        print('A string1 é maior')
    elif len(string1) < len(string2):
        print('A string2 é maior')
    else:
        print('As strings são iguais')

string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')

comparaString(string1, string2)
