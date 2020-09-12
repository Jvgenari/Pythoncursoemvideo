num = []
s = 'S'
while True:
    n = int(input(('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Número registrado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    s = str(input('Quer continuar? [S/N] ')).upper().strip()
    if s == 'N':
        break
    elif s not in 'SN':
        print('Somente [S/N]!!')
        s = str(input('Quer continuar? [S/N] ')).upper().strip()
num.sort()
print(f'Você digitou os valores {num}')
