teste = "Palavra"
print(teste[0:2])

frase = "Hoje está fazendo sol aqui em Floripa"
print(frase[18:21])

sol = frase[18:21]
print(sol)
print("Temos um dia de %s hoje" %sol)

nome = "Rafael"
print(nome[:4]) #Começa no index 0 até o index 4
print(nome[4:]) #Começa no index 4 até o final
print(nome[:])  #Começa no index 0 até final

# Começa da direita para esquerda
print(nome[0:-1]) #Rafae
print(nome[0:-3]) #Raf