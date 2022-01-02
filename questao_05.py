def pesquise(lista, valor):
	return valor if valor in lista else None

L=[10, 20, 25, 30] 

print(pesquise(L,10))
