import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input('Digite o ano da {}ª pessoa: '.format(i)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))
