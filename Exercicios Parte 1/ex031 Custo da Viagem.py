d = float(input('Digite a distância da sua viagem: '))

if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45
print('O preço da sua passagem será de {:.2f}'.format(v))