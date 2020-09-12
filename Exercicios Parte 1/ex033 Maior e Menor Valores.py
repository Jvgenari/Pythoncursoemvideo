n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if maior < n3:
    maior = n3

if menor > n3:
    menor = n3


print('O numero maior foi {}\nO numero menor foi {}'.format(maior, menor, ))
