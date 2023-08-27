produtoA = ["Produto 1", 50.00]
produtoB = ["Produto 2", 60.00]
produtoC = ["Produto 3", 45.00]

produtos = [produtoA, produtoB, produtoC]
print(produtos)

for produto in produtos:
    print("O nome do produto é %s e o preço do produto é %.2f: " %(produto[0], produto[1]))
