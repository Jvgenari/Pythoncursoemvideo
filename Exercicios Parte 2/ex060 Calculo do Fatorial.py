n = int(input('Digite um número: '))
c = n
fatorial = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial, end='')
