carro = {
    "portas": 4,
    "janelas": 4,
    "motor": 2.0,
    "tetosolar": True,
    "cambio": "automático"
}

print(carro)
print(carro['portas'])

#============== Verifica se a chave "chave" tem no dicionario ==============
pessoa = {
    "nome": "Rafael",
    "idade": 40
}

print(pessoa)
print("nome" in pessoa)
print("sobrenome" in pessoa)

if "nome" in pessoa:
    print("O seu nome é %s" %pessoa["nome"])
if "sobrenome" in pessoa:
    print("O seu sobrenome é %s" %pessoa["sobrenome"])
else:
    print("Não existe a chave sobrenome")

#============== Adiciona uma propriedade no dicionario ==============
pessoa["sobrenome"] = "Miranda"
if "sobrenome" in pessoa:
    print("O seu sobrenome é %s" %pessoa["sobrenome"])

#============== Remove uma propriedade no dicionario ==============
del pessoa["sobrenome"] 
if "sobrenome" in pessoa:
    print("O seu sobrenome é %s" %pessoa["sobrenome"])
