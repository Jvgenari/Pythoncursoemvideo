from random import randint
na = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print ('Os valores sorteados foram: ', end='')
for n in na:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteador foi {max(na)}')
print(f'O menor valor sorteador foi {min(na)}')
