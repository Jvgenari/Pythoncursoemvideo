maior = 0
sidade = 0
countm = 0
velho = ''
for i in range(1, 5):
    print('-' * 5 + ' {}ª Pessoa '.format(i) + '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    sidade += idade
    if idade > maior and sexo == 'M':
        maior = idade
        velho = nome
    elif idade < 20 and sexo == 'F':
        countm += 1
media = sidade / 4
print('A média de idade do grupo foi de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, velho))
print('Ao todo são {} mulheres com menos de 21 anos.'.format(countm))
