lista = ["Sofá","Televisão", "Rádio", "Poltrona"]
print(lista)

elementoEncontrar = input("O que deseja encontrar? ")
i = 0
achou = False
while i < len(lista):
    if lista[i] == elementoEncontrar:
       print("Elemento encontrado %s na posição %d" %(lista[i], i))
       achou = True
    i = i + 1
if achou == False:
    print("Não foi encontrado o elemento %s" %elementoEncontrar)