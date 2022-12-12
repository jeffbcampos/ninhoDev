def potencia(base, expoente):
    resultado = 1
    for i in range(expoente):
        resultado = resultado * base
        
    return resultado

print(potencia(3, 4))