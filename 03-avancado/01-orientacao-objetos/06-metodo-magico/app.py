class Pessoa:
  def __init__(self, nome, idade, profissao):
    self.nome = nome
    self.idade = idade
    self.profissao = profissao

  def __str__(self):
    return "O nome do usuário %s e tem %d anos e é um %s" % (self.nome, self.idade, self.profissao)

rafael = Pessoa("Rafael", 40, "Programador")

print(rafael.__str__())