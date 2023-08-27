lista = [1,2,3]
novaLista = []
novaLista = lista #Não copia a lista e sim faz uma referencia a outra lista

print(lista)
print(novaLista)

novaLista[0] = 1000 #Modifica o posição 0 das 2 lista, porque é referencia da primeira lista

print(lista)
print(novaLista)

lista[1] = 99 #Modifica o posição 1 das 2 lista, porque esta referenciado na segunda lista

print(lista)
print(novaLista)