def tip(conta):
    tip = (10 * conta) / 100
    return tip

conta = int(input("Digite o valor da conta: "))

print(f"A gorjeta será de {tip(conta)}")

