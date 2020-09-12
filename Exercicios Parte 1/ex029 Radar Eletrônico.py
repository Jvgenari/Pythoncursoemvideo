v = float(input('Escreva a velocidade do carro: '))

if v>80:
    m = (v - 80) * 7
    print('Você foi multado pelo valor de R${:.2f}!'.format(m))
else:
    print('Sua velocidade está dentro do limite.')

