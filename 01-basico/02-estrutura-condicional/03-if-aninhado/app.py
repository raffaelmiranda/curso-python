idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Você pode entrar na balada.")
    metodoPagamento = input("Como você vai pagar a entrada? ")
    if metodoPagamento == "dinheiro":
        print("A fila do dinheiro é a numero 1")
    else:
        print("A fila de cartão é a numero 2")
else:
    print("Você não pode entrar na balada.")