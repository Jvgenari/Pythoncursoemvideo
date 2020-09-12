maior = 0
menor = 0
count1 = 0
count2 = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
        count1 = i
        menor = peso
    elif peso < menor:
        menor = peso
        count2 = i
print('O MAIOR peso foi de {}Kg da pessoa nº{}'.format(maior, count1))
print('O MENOR peso foi de {}Kg da pessoa nº{}'.format(menor, count2))
