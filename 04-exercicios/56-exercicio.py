def ReuneDados(nome, idade, profissao, fnct):
    apresentacao = fnct(nome, idade, profissao)
    return apresentacao
def ApresentaDados(nome, idade, profissao):
    return "O nome do é usuário %s e sua idade é %d ele é um %s" %(nome, idade, profissao)

print(ReuneDados("Rafael", 40, "Programador", ApresentaDados))