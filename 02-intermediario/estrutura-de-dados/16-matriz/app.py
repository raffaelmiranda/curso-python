carroA = ["BMW", 5000]
carroB = ["Ferrari", 60000]
carroC = ["VW", 45000]

carros = [carroA, carroB, carroB]
print(carros)
print(carros[0][0])
print(carros[0][1])
print(carros[2][0])

for carro in carros:
    print("A marca do carro é: %s" %carro[0])