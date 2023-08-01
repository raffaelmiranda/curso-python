tupla = (1,2,3)
print(tupla)
print(type(tupla))

#tupla[0] = 1 #Erro de atribuição, não é permitido
print(tupla[2])

for item in tupla:
    print(item)

i = 0
while i < len(tupla):
  print(tupla[i])
  i = i + 1