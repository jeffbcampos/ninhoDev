def pagamento(qtd_horas, valor_hora):
    if qtd_horas <= 40:
        salario = 40 * valor_hora
    else:
        extra = qtd_horas - 40
        salario = 40 * valor_hora + (extra * (valor_hora * 1.5))
    return salario

horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valorHora = float(input("Digite o valor da sua hora: "))

print(pagamento(horasTrabalhadas, valorHora))