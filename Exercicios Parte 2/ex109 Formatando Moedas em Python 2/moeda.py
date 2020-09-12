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
