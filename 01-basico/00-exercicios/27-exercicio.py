renda = float(input("Digite a Renda? "))
limite = 0
if renda < 2000:
    limite = 1000
elif renda < 4000:
    limite = 2000
elif renda < 10000:
    print("Falar com o gerente")
    limite = 3000
print("O seu cartão foi aprovado e o limite e de R$%d" %limite)