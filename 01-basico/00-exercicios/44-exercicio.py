numeros = [100,200,400,500,700]
numeroEncontrar = int(input("Qual número deseja buscar? "))
encontrado = False
for n in numeros:
    if n == numeroEncontrar:
        print("O numero %d foi encontrado!" %n)
        encontrado = True
if encontrado == False:
    print("Não encontramos o número %d" %numeroEncontrar)