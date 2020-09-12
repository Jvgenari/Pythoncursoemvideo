from random import randint
cont = 1
computador = randint(0, 10)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 a 10.\nSerá que você consegue adivinhar qual foi?')
jogador = int(input('Qual seu palpite? '))
while jogador != computador:
    if jogador < computador:
        cont += 1
        print('Mais... Tente mais uma vez!')
        jogador = int(input('Qual é seu palpite? '))
    else:
        cont += 1
        print('Menos... Tente mais uma vez!')
        jogador = int(input('Qual é seu palpite? '))
print('Acertou com {} tentativa(s). Parabéns!'.format(cont))
