#1) Escreva uma função que retorne o maior de dois números. Valores esperados:
#máximo(5,6) == 6
#máximo(2,1) == 2
#máximo(7,7) == 7

def maior(a,b):
    
    if a > b:
        print("O valor a e maior",a)
    else:
        print("O valor b e maior",b)

a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

maior(a,b)

