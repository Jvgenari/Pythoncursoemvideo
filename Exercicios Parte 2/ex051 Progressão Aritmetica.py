t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = t + (10 - 1) * r
for i in range(t, décimo + r, r):
    t+= r
    print('{} -> '.format(i), end='')
print('ACABOU')
