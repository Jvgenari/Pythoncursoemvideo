from random import randint
from time import sleep
jogo = []
lista = []
n = 0
j = int(input('Quantos jogos? '))
while j != 0:
    while len(jogo) != 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    lista.append(jogo[:])
    jogo.clear()
    j -= 1
print('-=' * 3 + f'  SORTEANDO {len(lista)} JOGOS  ' + '-=' * 3)
for i in range(0, len(lista)):
    print(f'Jogo {i+1}: {lista[i]}')
    sleep(0.5)
print('-=' * 5 + f' < BOA SORTE! >  ' + '-=' * 5)
