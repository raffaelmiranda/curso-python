class Veiculo:
  def __init__(self, rodas, marca):
    self.rodas = rodas
    self.marca = marca
  def ligar(self):
    print("Vrummmm")
  def mudarPreco(self, novoPreco):
    self.preco = novoPreco

class Carro(Veiculo):
  def __init__(self, rodas, marca, tetoSolar):
    super().__init__(rodas, marca)
    self.tetoSolar = tetoSolar

class Moto(Veiculo):
  def __init__(self, rodas, marca, protecao):
    super().__init__(rodas, marca)
    self.protecao = protecao
  def empinar(self):
    print("Empinou a moto")

ferrari = Carro(4, "Ferrari", True)
print(ferrari.marca)
ferrari.ligar()
print(ferrari.tetoSolar)

honda = Moto(2, "Honda", False)
print(honda.marca)
honda.ligar()
honda.empinar()
print(honda.protecao)