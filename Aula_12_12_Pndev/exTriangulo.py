class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def getMaiorLado(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return self.lado1
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            return self.lado2
        else:
            return self.lado3

lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))

triangulo = Triangulo(lado1, lado2, lado3)

print(f'O perímetro do triângulo é {triangulo.perimetro()}')

print(f'O maior lado do triângulo é {triangulo.getMaiorLado()}')

