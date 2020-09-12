from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = {}
for c in range(0, 4):
    jogadores[f'jogador[{c+1}]'] = randint(1, 6)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados:')
for i, v in jogadores.items():
    print(f'   {i} tirou {v} no dado.')
    sleep(1)
print('Ranking dos Jogadores:')
for k, v in enumerate(ranking):
    print(f'   {k+1}º lugar: {v[0]} com {v[1]}.')
