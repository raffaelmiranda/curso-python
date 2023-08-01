def Multiplicacao(*nums):
    resultado = 1
    for num in nums:
      resultado *= num
    return resultado

resultado = Multiplicacao(5, 4, 3, 2, 66, 5, 64)
print(resultado)