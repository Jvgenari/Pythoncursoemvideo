par = impar = 0
c = 1
while c!=0:
    c = int(input('Digite um número: '))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} pares e {} impares'.format(par, impar))
'''''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''''