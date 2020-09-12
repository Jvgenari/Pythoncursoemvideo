n = int(input('Primeiro termo: '))
r = int(input('Razão da PA?: '))
c = 1
while c < 11:
    print('{} -> '.format(n), end='')
    n += r
    c += 1
print('FIM', end='')
