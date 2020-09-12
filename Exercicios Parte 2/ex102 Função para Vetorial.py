def fatorial(a, b=False):
    '''

    :param a: Número a ser fatorado
    :param b: (opcional) Boolean para saber se quer mostrar os numeros fatorados
    :return: retorna o numero fatorado
    '''
    fat = 1
    for c in range(a, 0, -1):
        if b == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat




print(fatorial(5, True))
