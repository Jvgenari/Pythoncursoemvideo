valores = []
count = menor = maior = 0
pmaior = []
pmenor = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] < menor:
            menor = valores[c]
        if valores[c] > maior:
            maior = valores[c]

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(valores):
    if menor == v:
        pmenor.append(i)
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if maior == v:
        pmaior.append(i)
        print(f'{i}... ', end='')
