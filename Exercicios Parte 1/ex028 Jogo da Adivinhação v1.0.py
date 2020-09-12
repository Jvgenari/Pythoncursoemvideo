from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabens, você acertou!')
else:
    print('Errou! Eu pensei no {} e não no {}'.format(computador, jogador))
