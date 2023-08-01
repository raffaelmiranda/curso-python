saque = int(input("Digite o quanto quer sacar: "))

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

while saque > 0:
    while saque >= 100:
        nota100 = nota100 + 1
        saque = saque - 100
    while saque >= 50:
        nota50 = nota50 + 1
        saque = saque - 100
    while saque >= 20:
        nota20 = nota20 + 1
        saque = saque - 20
    while saque >= 10:
        nota10 = nota10 + 1
        saque = saque - 10
    while saque >= 1:
        nota1 = nota1 + 1
        saque = saque - 1
print("Você vai receber %d notas de R$100, %d notas de R$50, %d notas de R$20, %d notas de R$10, %d notas de R$1"  %(nota100, nota50, nota20, nota10, nota1))