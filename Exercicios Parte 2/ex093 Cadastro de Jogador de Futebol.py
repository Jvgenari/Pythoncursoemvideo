jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for c in range (1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for i, v in jogador.items():
    print(f'O campo {i} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, j in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {j} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
