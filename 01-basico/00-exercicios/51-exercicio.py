def verificaNumeroMaior(numero):
    resultado = ""
    if numero > 10:
        resultado = "Maior que 10"
    elif numero < 10:
        resultado = "Menor que 10"
    else:
        resultado = "Igual a 10"
    return resultado
resultado = verificaNumeroMaior(4)
print(resultado)
resultado = verificaNumeroMaior(10)
print(resultado)
resultado = verificaNumeroMaior(15)
print(resultado)