def aumentar(f=0, n=0):
    f += (f/100 * n)
    return f


def metade(f=0):
    f /= 2
    return f


def dobro(f=0):
    f *= 2
    return f


def diminuir(f=0, n=0):
    f -= (f/100 * n)
    return f


def moeda(f=0, moeda='R$'):
    return f'{moeda}{f:.2f}'.replace('.', ',')
