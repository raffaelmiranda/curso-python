def CalculaMedia(lista):
  soma = 0
  media = 0
  for numero in lista:
    soma += numero
  media = soma / len(lista)
  return media

lista =[4,7,9,2,10,7,10]
retorno = CalculaMedia(lista)
print("A média da lista é: %.2f" %retorno)