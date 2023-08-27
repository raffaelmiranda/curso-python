def VerificaNumeroPares(lista):
  numerosPares = []
  for numero in lista:
    if numero % 2 == 0:
      numerosPares.append(numero)
  return numerosPares

def VerificaNumeroImpares(lista):
  numerosImpares = []
  for numero in lista:
    if numero % 2 == 1:
      numerosImpares.append(numero)
  return numerosImpares

lista = [1,2,3,4,5,6,7,8,9,0]

numerosPares = VerificaNumeroPares(lista)
print(numerosPares)

numerosImpares = VerificaNumeroImpares(lista)
print(numerosImpares)