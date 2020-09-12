n = int(input('Primeiro termo: '))
r = int(input('Razão da PA?: '))
c = 1
t = 1
cont = 10
while not t == 0:
    while c < 11:
        print('{} -> '.format(n), end='')
        n += r
        c += 1
        if c == 11:
            print('PAUSA', end='')
            t = int(input('\nQuantos termos você quer a mais? '))
            c -= t
            cont += t
print('Progressão finalizada com {} termos mostrados.'.format(cont), end='')
