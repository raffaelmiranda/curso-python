def Soma(*nums):
    soma = 0
    for num in nums:
      soma += num
    return soma

resultado = Soma(5, 4, 3, 2, 66, 5, 64)
print(resultado)