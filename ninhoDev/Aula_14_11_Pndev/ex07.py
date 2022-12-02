sal = float(input("Digite o valor do seu salário: "))
fin = float(input("Digite o valor do financiamento pretendido: "))

if(fin <= (5 * sal)):
    print("Financiamento concedido, obrigado por nos consultar")
else:
    print("Financiamento negado, obrigado por nos consultar")
