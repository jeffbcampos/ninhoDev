def tip(conta):
    tip = (10 * conta) / 100
    return tip

valor = float(input("Digite o valor da conta: "))

print(f"A gorjeta será de R$ {tip(valor):.2f} reais")


