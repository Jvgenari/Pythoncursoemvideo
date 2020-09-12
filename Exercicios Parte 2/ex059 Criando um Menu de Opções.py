from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
maior = 0
c = 0
while not c == 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    c = int(input('Qual é a sua opção? '))
    if c == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif c == 2:
        mult = n1 * n2
        print('O resultado entre {} x {} é {}'.format(n1, n2, mult))
    elif c == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif c == 4:
        print('Qual são os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção Inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Finalizando...')
print('=-=' * 10)
print('Fim do programa! Volte sempre!')

