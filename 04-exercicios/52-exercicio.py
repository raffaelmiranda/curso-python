def ChecaTamanhoTexto(texto):
    retorno = ""
    if len(texto) > 20:
        retorno = "Texto muito longo!"
    else:
        retorno = "Texto curto"
    return retorno

retorno = ChecaTamanhoTexto("O Rafael Miranda é um programador")
print(retorno)

retorno = ChecaTamanhoTexto("Estou com fome")
print(retorno)