#Dada uma palavra, retorna a palavra invertida

word = input("Digite uma palavra para poder inverte-la: ")
wordInvert = ''

for i in range(len(word) - 1, -1, -1):
    wordInvert += word[i]
print(wordInvert)