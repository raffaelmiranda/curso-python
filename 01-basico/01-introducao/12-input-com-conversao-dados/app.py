numeroInteiroTexto = input("Digite um número: ")
numero1 = int(numeroInteiroTexto)
print(numero1 + 5)

numeroDecimalTexto = input("Digite o valor em decimal: ")
numero2 = float(numeroDecimalTexto)
print(numero2 + 5)

salario = float(input("Digite o salário (R$): "))
aumento = float(input("Digite o aumento (%): "))
resultado = salario + (salario * (aumento / 100))
print("O aumento de %.2f do salário R$%.2f é R$%.2f"  %(aumento, salario, resultado))

base = int(input("Digite a base: "))
expoente = int(input("Digite a expoente: "))
calculo = base ** expoente
print("O resultado da potência é %d" %calculo)