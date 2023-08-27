itensCarro = ["Porta","Pneu","Estepe","Maçaneta","Janela","Chave","Motor","Marcha",]

item1 = input("O que deseja procurar primeiro? ")
item2 = input("O que deseja procurar depois? ")

i = 0
while i < len(itensCarro): 
    if itensCarro[i] == item1:
      print("O primeiro objeto foi encontrado antes! %s" %item1)
      break
    elif itensCarro[i] == item2:
      print("O segundo objeto foi encontrado antes! %s" %item2)
      break
    i = i + 1
    