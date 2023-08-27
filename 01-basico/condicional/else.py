poupanca = 200
saque = int(input("Quando deseja sacar? "))

if saque <= poupanca:
    print("Você sacou R$%d reais" %saque)
else:
    print("Você não tem saldo para sacar R$%d" %saque)
    print("Sua poupança tem no momento R$%d" %poupanca)