lista = []
v = False
while True:
    lista.append(int(input('Digite um valor: ')))
    s = str(input('Quer continuar? [S/N] ')).strip().upper()
    if s == 'N':
        break
    elif s not in 'SN':
        print('Somente [S/N]!!')
        s = str(input('Quer continuar? [S/N] ')).upper().strip()
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em descrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
