from random import randint
from time import sleep


def sorteia(list):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        list.append(n)
        print(f'{list[c]} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somapar(list):
    soma = 0
    for c in range(0, len(list)):
        if list[c] % 2 == 0:
            soma += list[c]
    print(f'Somando os valores pares de {list}, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)
