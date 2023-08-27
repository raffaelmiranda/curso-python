class Pessoa:
  def __init__(self, nome, sobrenome, idade):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade

pessoa = Pessoa("Rafael", "Miranda", 40)
print(type(pessoa))
print(pessoa.nome)
print(pessoa.sobrenome)
print(pessoa.idade)