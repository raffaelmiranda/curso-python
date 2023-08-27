class Banco:
  def __init__(self, nome, saldo):
    self.nome = nome
    self.saldo = saldo
  def deposito(self, valor):
    self.saldo += valor
  def saque(self, valor):
    self.saldo -= valor
  def transferencia(self, conta, valor):
    self.saldo -= valor
    conta.saldo += valor

conta1 = Banco("Rafael", 1000)
print(conta1.nome)

conta1.deposito(500)
print(conta1.saldo)

conta1.saque(49)
print(conta1.saldo)

conta2 = Banco("Maria", 100)
print(conta2.nome)

conta1.transferencia(conta2, 200)

print(conta1.saldo)
print(conta2.saldo)
