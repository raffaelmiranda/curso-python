class Carro:
  def __init__(self, marca, preco, numeroPorta, tanque):
    self.marca = marca
    self.preco = preco
    self.numeroPorta = numeroPorta
    self.tanque = tanque
  def abastecer(self, litros):
    if self.tanque >= 100:
      print("Taque está cheio")
    else:
      self.tanque += litros
      if self.tanque > 100:
        self.tanque = 100
  def dirigir(self, km):
    kmPorLitro = 10
    self.tanque -= (km / kmPorLitro)

fusca = Carro("VW", 60000, 4, 80)

print(fusca.tanque)
fusca.abastecer(10)
print(fusca.tanque)
fusca.dirigir(10)
print(fusca.tanque)