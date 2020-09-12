c = ''
soma = cont = media = maior = menor = 0
while c != 'N':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
media = soma / cont

print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
