def area(a, b):
    ar = a * b
    print(f'A área de um terreno {a}x{b} é de {ar}.')


print('  Controle de Terrenos')
print('-' * 20)
lar = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(lar, c)
