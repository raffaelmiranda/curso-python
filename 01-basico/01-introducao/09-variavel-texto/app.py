profissao = "Programador"
print(profissao)
print('Programador')

frase = "O rato roeu a roupa do Rei de Roma"
print(frase)

#============ Tamanho do texto ============
print(len(frase))

#============ Acessando os caracteres ============
print(frase[3])
print(frase[11])
#print(frase[111]) #string index out of range

#============ Concatenação de texto ============
nome = 'Rafael'
print('Ola ' + nome)

velocidade = '200'
carro = "Ferrari"
cidade = "Floripa"
print('O veiculo ' + carro + ' estava a ' + velocidade + 'km/h em ' + cidade)

#============ Strings dinamicas ============
print('Olá, meu nome é %s' % nome)

idade = 29
print('Eu tenho %d anos' % idade)

carro = "Ferrari"
ano = 2000
print('O meu carro é uma %s e foi fabricado no ano %d' %(carro,ano))

pi = 3.1439247237842873478
print('O valor de pi é %f' %pi)
print('O valor de pi é %.10f' %pi)
print('O valor de pi é %.2f' %pi)