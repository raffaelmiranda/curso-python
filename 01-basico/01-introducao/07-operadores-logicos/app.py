print('================ NOT ================')
verdadeiro = True
falso = False

print(not verdadeiro)
print(not falso)
print(not(5>2))
print(not(5<2))

print('================ AND ================')
a = 5
b = 10
c = 2
d = 8

print(a > b and c > d)
print(a > b and c < d)
print(c > d and b < c)
print(c < b and b > c)

print('================ OR ================')
print(a > b or b == 11)
print(b > a or b == 10)
print(a > b or b == 10)
print(b > a or b == 20)