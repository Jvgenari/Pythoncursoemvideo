print('=' * 30)
print(' ' * 10 + 'BANCO CEV' + ' ' * 10)
print('=' * 30)
cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Que valor você quer sacar? R$'))
while True:
    if valor - 50 >= 0:
        cont50 += 1
        valor -= 50
    elif valor - 20 >= 0:
        cont20 += 1
        valor -= 20
    elif valor - 10 >= 0:
        cont10 += 1
        valor -= 10
    else:
        cont1 += 1
        valor -= 1
    if valor == 0:
        break
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
