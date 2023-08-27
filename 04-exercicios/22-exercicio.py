numero1 = int(input("Digite o 1º numero: "))
numero2 = int(input("Digite o 2º numero: "))

if numero1 > numero2:
    print("O número %d é maior que o número %d" %(numero1, numero2))
if numero2 > numero1:
    print("O número %d é maior que o número %d" %(numero2, numero1))
if numero2 == numero1:
    print("O número %d é igual o número %d" %(numero1, numero2))