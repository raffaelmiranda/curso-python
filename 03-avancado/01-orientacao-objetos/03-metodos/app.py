class Carro:
  def __init__(self, marca, preco):
    self.marca = marca
    self.preco = preco
  def ligar(self):
    print("Vrummmm")
  def mudarPreco(self, novoPreco):
    self.preco = novoPreco

polo = Carro("VW",60000)

print(polo.marca)
polo.ligar()
polo.mudarPreco(90000)
print(polo.preco)