# 5.Receba dois números inteiros correspondentes à largura e altura. Devolva uma
# cadeia de caracteres # que representa um retângulo com as medidas fornecidas.

# # # # # # #
#           #
# # # # # # #

caract = "#"
larg = int(input("Digite a largura do retangulo: "))
alt = int(input("Digite a altura do retangulo: "))
topRect = (caract * larg) + "\n"
medRect = (caract + (' ' * (larg - 2)) + caract + "\n") * (alt - 2)

print(topRect + medRect + topRect)

print(((larg * caract) + "\n") * alt)