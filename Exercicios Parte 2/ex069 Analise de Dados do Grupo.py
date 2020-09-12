adulto = homem = mulher = 0

while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade? '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        adulto += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade > 20:
        mulher += 1
    print('-' * 25)
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).upper().strip()
    if c == 'N':
        break
print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {adulto}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
