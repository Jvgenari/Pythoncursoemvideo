jogador = {}
jogadores = []
cod = 0
while True:
    jogador['cod'] = cod
    cod +=1
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for c in range (1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    s = str(input('Quer continuar? [S/N] ')).upper().strip()
    while s not in 'SN':
        print('Somente [S/N]')
        s = str(input('Quer continuar? [S/N] ')).upper().strip()
    if s == 'N':
        break

print('-=' * 30)
print(f'cod  {"nome":<8}  {"gols":<8}{"total":<8}')
print('-' * 26)
for c in jogadores:
    for v in c.values():
        print(f'{v}  ', end='')
    print()
print('-' * 26)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar!) '))
    if n == 999:
        break
    elif n > len(jogadores) or n < 0:
        print(f'ERRO! Não existe este jogador com código {n}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[n]["nome"]}:')
        for i, j in enumerate(jogadores[n]['gols']):
            print(f'No jogo {i+1} fez {j} gols.')
print('<< VOLTE SEMPRE >>')