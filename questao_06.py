#6) Reescreva o programa da abaixo de forma a utilizar for em vez de while.

def soma(L):
    total = 0
    for e in L:
      total+=e
    return total

L=[10,12,20]
print(soma(L))