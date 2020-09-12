valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    s = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if valores[-1] % 2 == 0:
        par.append(valores[-1])
    else:
        impar.append(valores[-1])
    if s == 'N':
        break
    elif s not in 'SN ':
        print('Somente [S/N]!!!')
        s = str(input('Quer continuar ? [S/N] ')).upper().strip()
print('-=' * 30)

print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')