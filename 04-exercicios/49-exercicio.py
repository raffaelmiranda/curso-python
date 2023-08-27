carro = {
    "pneu": 4,
    "portas": 2,
    "motor": 1,
    "janela": 4
}

print(carro)
carro["tetosolar"] = 1

print(carro)
print(["tetosolar"])

del carro["motor"]
del carro["janela"]
print(carro)