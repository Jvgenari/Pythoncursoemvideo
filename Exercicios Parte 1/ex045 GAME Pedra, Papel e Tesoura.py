import random
import time
print('Suas Opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('Qual sua jogada? '))
if jogador > 2:
    print('JOGADA INVALIDA!')
    exit(-1)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
computador = random.randint(0, 2)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('-=' * 11)
print('COMPUTADOR jogou {}'.format(lista[computador]))
print('JOGADOR jogou {}'.format(lista[jogador]))
print('-=' * 11)
if jogador == 0 and computador == 1:
    print('\033[;30;41mJOGADOR PERDEU!!\033[m')
elif jogador == 0 and computador == 2:
    print('\033[;30;42mJOGADOR GANHOU!!\033[m')
elif jogador == 1 and computador == 0:
    print('\033[;30;42mJOGADOR GANHOU!!\033[m')
elif jogador == 1 and computador == 2:
    print('\033[;30;41mJOGADOR PERDEU!!\033[m')
elif jogador == 2 and computador == 0:
    print('\033[;30;41mJOGADOR PERDEU!!\033[m')
elif jogador == 2 and computador == 1:
    print('\033[;30;42mJOGADOR GANHOU!!\033[m')
elif jogador == computador:
    print('\033[;30;46mEMPATOU!!\033[m')
