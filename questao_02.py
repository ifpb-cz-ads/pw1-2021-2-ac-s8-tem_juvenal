#2) Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

#Valores esperados:
#múltiplo(8,4) == True
#múltiplo(7,3) == False
#múltiplo(5,5) == True

def multiplo(a,b):
    
    if a%b==0:
        return True
    else:
        return False

a = int(input("Digite um valor inteiro: "))
b = int(input("Digite outro valor inteiro: "))
print(multiplo(a,b))