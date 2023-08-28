"""
1. (n + n)   - Parênteses
2. **        - Exponenciação
3. * / // %  - Multiplicação, divisão, divisão inteira e módulo, que possuem a mesma precedência
4. +         - Adição e subtração, que possuem a mesma precedência

Operadores com a mesma precedência são avaliados da esquerda para a direita
"""

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

conta_2 = 5*3+10
print(conta_2)

conta_3 = 10+2/3
print(conta_3)

conta_4 = 12+4-(10/2)
print(conta_4)