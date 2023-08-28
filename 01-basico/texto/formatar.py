a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

#==== 1º Forma (format)====
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)

#==== 2º Forma (f-strings)====
print(f'Valor de A {a}')
print(f'Valor de B {b}')

#==== 3º Forma (dinamico)====
print('Valor de A %s' %(a))
print('Valor de B %s' %(b))
print('Valor de C %.2f' %(c))