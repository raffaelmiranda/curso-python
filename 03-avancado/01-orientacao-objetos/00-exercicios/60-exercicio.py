class Carro:
  def __init__(self, portas, motor, tetoSolar, marca, preco):
    self.portas = portas
    self.motor = motor
    self.tetoSolar = tetoSolar
    self.marca = marca
    self.preco = preco

print("Criando carro da Volkswagen")
polo = Carro(4, 1.0, True, "Volkswagen", 70000)
print(polo.portas)
print(polo.motor)
print(polo.tetoSolar)
print(polo.marca)
print(polo.preco)

print("Criando carro da Ferrari")
ferrari = Carro(2, 3.0, True, "Ferrari", 250000)
print(ferrari.portas)
print(ferrari.motor)
print(ferrari.tetoSolar)
print(ferrari.marca)
print(ferrari.preco)