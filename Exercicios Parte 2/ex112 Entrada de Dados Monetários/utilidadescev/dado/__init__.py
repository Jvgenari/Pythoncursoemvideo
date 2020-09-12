def leiadinheiro(s):
    valido = False
    while not valido:
        f = str(input(s)).replace(',', '.').strip()
        if f.isalpha() or f == '':
            print(f'\033[0;31mERRO! \"{f}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(f)
