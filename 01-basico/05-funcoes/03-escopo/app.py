escopoGlobal = "Global"

def EscopoLocal():
    escopoLocal = "Local"
    print("Váriavel de escopo local dentro da função: %s" %escopoLocal)
    print("Váriavel de escopo global dentro da função: %s" %escopoGlobal)

EscopoLocal()

print("Váriavel de escopo global fora da função: %s" %escopoGlobal)
#print("Váriavel de escopo local dentro da função: %s" %escopoLocal) #Erro

escopoGlobal = "Mudando o valor"
print(escopoGlobal)
