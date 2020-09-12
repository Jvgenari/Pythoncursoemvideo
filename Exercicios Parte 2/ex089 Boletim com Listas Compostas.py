from time import sleep
aluno = []
cadastro = []
med = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    cadastro.append(aluno[:])
    aluno.clear()
    s = str(input('Quer continuar? ')).upper().strip()
    if s == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for c in range(0, len(cadastro)):
    media = (cadastro[c][1] + cadastro[c][2]) / 2
    med.append(media)
    media = 0
    print(f'{c:<4}{cadastro[c][0]:<10}{med[c]:8.1f}')
while True:
    print('-' * 35)
    a = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if a == 999:
        break
        print('FINALIZANDO...')
    else:
        print(f'Notas de {cadastro[a][0]} são {cadastro[a][1:]}')
sleep(0.5)
print('<<< VOLTE SEMPRE >>>')
