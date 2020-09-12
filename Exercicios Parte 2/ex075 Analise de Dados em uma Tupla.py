n = (int(input('Digite um número: ')),
     int(input('Digite o segundo número: ')),
     int(input('Digite o terceiro número: ')),
     int(input('Digite o ultimo número: ')))
count = max = min = 0

print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro valor 3 ficou na posição {n.index(3) + 1}')
else:
    print('O número 3 não foi digitado.')

print(f'Os números pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
