lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = []

i = 0
while i < len(lista1):
    lista3.append(lista1[i])
    i = i + 1
i = 0
while i < len(lista2):
    lista3.append(lista2[i])
    i = i + 1

print(lista3)