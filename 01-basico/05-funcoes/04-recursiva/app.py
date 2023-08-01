def soma(numero):
  if numero < 100:
    numero += 1
    print(numero)
    return soma(numero)
  else:
    return numero

somado = soma(94)
print(somado)
      