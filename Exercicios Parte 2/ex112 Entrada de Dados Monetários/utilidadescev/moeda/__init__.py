def aumentar(f=0, n=0, b=False):
    f += (f/100 * n)
    if b == True:
        return moeda(f)
    else:
        return f


def metade(f=0, b=False):
    f /= 2
    if b == True:
        return moeda(f)
    else:
        return f


def dobro(f=0, b=False):
    f *= 2
    if b == True:
        return moeda(f)
    else:
        return f


def diminuir(f=0, n=0, b=False):
    f -= (f/100 * n)
    if b == True:
        return moeda(f)
    else:
        return f


def moeda(f=0, moeda='R$'):
    return f'{moeda}{f:.2f}'.replace('.', ',')

def resumo(f=0, a=10, r=5):
    print('-' * 30)
    print('RESUMO DO VALOR:'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(f)}')
    print(f'Dobro do preço: \t{dobro(f, True)}')
    print(f'Metade do preço: \t{metade(f, True)}')
    print(f'{a}% de aumento: \t{aumentar(f, a, True)}')
    print(f'{r}% de redução: \t{diminuir(f, r, True)}')
    print('-' * 30)
