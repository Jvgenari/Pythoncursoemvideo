#Exemplo de importação de bibliotecas

from math import sqrt, floor

num = int(input('Digite um número: '))

raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

import random
num = random.random()
num2 = random.randint(1, 65)
print(num, num2)
