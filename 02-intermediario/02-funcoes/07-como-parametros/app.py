def soma(a, b):
    return a + b
def multiplicacao(a, b):
    return a * b
def operacao(a, b, f):
    return f(a, b)

retorno = operacao(5, 5, soma)
print(retorno)

retorno = operacao(5, 5, multiplicacao)
print(retorno)