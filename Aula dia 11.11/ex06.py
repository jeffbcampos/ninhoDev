

menu = {
    100: 1.10,
    101: 1.30,
    102: 1.50,
    103: 1.10,
    104: 1.30,
    105: 1.00
}
prod = {
    100: "Hot Dog",
    101: "Bauru simples",
    102: "Bauru c/ovo",
    103: "Hamburger",
    104: "Cheeseburger",
    105: "Refrigerante"
}

print(f'''Good Burger, A casa do Hamburger, Posso Anotar o seu pedido:
Este é o nosso menu:
{"-=" * 20}

100 - {prod[100]} - Valor: {menu[100]:.2f}
101 - {prod[101]} - Valor: {menu[101]:.2f}
102 - {prod[102]} - Valor: {menu[102]:.2f}
103 - {prod[103]} - Valor: {menu[103]:.2f}
104 - {prod[104]} - Valor: {menu[104]:.2f}
105 - {prod[105]} - Valor: {menu[105]:.2f}

{"-=" * 20}
''')

pedido = int(input("Digite o número do seu pedido: "))
qtd = int(input("Digite a quantidade do seu pedido: "))

print(f"Você pediu {qtd} {prod[pedido]} - Valor do seu pedido: {qtd * menu[pedido]:.2f}")

