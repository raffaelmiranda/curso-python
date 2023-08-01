lista = [1,2,3]
novaLista = lista[:] #Copia todos os elementos

print(lista)
print(novaLista)

novaLista[0] = 1000 
print(novaLista)

lista[1] = 99
print(lista)
