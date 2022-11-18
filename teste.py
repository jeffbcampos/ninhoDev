produtos = {100: dict(name = 'Dog', price=1.50), 101: 'Água', 102: 'Chess', 103: 'Bauru'}
price = {100: 1.50, 101: 1.30, 102: 1.20, 103: 1.10}



pedido = int(input("Digite o número do seu pedido: "))
qtd = int(input("Digite a quantidade: "))

print(f"O seu pedido foi {qtd} {produtos[pedido]}")