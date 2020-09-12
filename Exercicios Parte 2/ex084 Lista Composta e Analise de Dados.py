pessoas = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor = temp[1]
    else:
        if temp[1] >= maior:
            maior = temp[1]
        if temp[1] <= menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    s = str(input('Quer continuar? [S/N] ')).upper().strip()
    if s not in 'SN':
        print('Somente [S/N]!!!')
        s = str(input('Quer continuar? [S/N] ')).upper().strip()
    elif s == 'N':
        break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end='')
for p in pessoas:
    if p[1] == menor:
        print(f' {p[0]}', end='')