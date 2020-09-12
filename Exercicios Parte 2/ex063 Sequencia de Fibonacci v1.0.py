t = int(input('Quantos termos você quer mostrar? '))
n = 0
n2 = 1
c = 3
print('{} - {}'.format(n, n2), end='')
s = n + n2
while not c == t+1:
    s = n + n2
    print(' - {}'.format(s), end='')
    c += 1
    n = n2
    n2 = s
print(' - FIM')
