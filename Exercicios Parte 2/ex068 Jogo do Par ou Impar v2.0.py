from random import randint
cont = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('=-' * 15)
    jogador = int(input('Diga um valor: '))
    s = str(input('Par ou Impar? [P/I]: ')).upper().strip()
    print('-' * 30)
    computador = randint(1, 10)
    if jogador <= 10:
        if (jogador + computador) % 2 == 0:
            if s == 'I':
                print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU PAR')
                break
            else:
                cont += 1
                print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU PAR')
                print('Você VENCEU!')
        if (jogador + computador) % 2 != 0:
            if s == 'P':
                print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU IMPAR')
                break
            else:
                cont += 1
                print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU IMPAR')
                print('Você VENCEU!')
    else:
        print('Valor errado! Só pode de 1 á 10!')
    print('Vamos jogar novamente...')
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vez(es).')
