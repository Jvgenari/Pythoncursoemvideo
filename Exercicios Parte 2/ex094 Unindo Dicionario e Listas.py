cadastro = {}
pessoas = []
idades = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    cadastro['idade'] = int(input('Idade: '))
    idades += cadastro['idade']
    pessoas.append(cadastro.copy())
    cadastro.clear()
    s = str(input('Quer continuar? [S/N] ')).upper().strip()
    while s not in 'SN':
        print('Erro! Responda apenas S ou N.')
        s = str(input('Quer continuar? [S/N] ')).upper().strip()
    if s == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = idades / len(pessoas)
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end='')
print('\nD) Lista das pessoas que estão acima da média:')
for c in pessoas:
    if c['idade'] >= media:
        print('    ', end='')
        for i, v in c.items():
            print(f'{i} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
