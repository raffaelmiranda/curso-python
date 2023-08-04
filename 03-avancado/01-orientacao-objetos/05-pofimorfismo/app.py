class Pessoa:
  def falar(self):
    print("Olá pessoal!")

class Rafael(Pessoa):
  def falar(self):
    print("Olá pessoal, eu sou o Rafael!")

class Roberto(Pessoa):
  pass

rafael = Rafael()
rafael.falar()

roberto = Roberto()
roberto.falar()
    