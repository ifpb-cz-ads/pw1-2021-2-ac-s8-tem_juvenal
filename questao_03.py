#3) Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado^2).

#Valores esperados:
#área_quadrado(4) == 16
#área_quadrado(9) == 81

def area(l):
    return l**2


l = float(input("Digite o lado:"))
a = area(l)
print(f"A ariea é = {a:4.0f}")
