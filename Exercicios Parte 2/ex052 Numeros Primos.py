n = int(input('Digite um número: '))
cont = 0
for i in range(n, 0, -1):
    print('{} '.format(i), end='')
    if n % i == 0:
        cont += 1
print('\nO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é primo!')
