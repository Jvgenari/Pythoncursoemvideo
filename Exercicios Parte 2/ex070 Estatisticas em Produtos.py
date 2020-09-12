print('-' * 30)
print(' ' * 5 + 'LOJA SUPER BARATÃO' + ' ' * 10)
print('-' * 30)
soma = cont = menor = contp = 0
pnome = ''

while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    soma += preço
    contp += 1
    if contp == 1:
        menor = preço
    if preço > 1000:
        cont += 1
    if preço < menor:
        menor = preço
        pnome = nome
        pvalor = preço
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).upper().strip()
    if c == 'N':
        break
print('-' * 15 + 'FIM DO PROGRAMA' + '-' * 15)

print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {pnome} que custa R${pvalor:.2f}')
