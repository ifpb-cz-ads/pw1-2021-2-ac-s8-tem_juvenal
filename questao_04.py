#4) Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2).

#Valores esperados:
#área_triângulo(6, 9) == 27
#área_triângulo(5, 8) == 20

def areaTriangulo(b,a):
    a = (b*a)/2
    return a

b = float(input("Digite a base: "))
l = float(input("Digite a altura: "))

a = areaTriangulo(b,l)

print(f"Área do triângulo={a:7.0f}")
