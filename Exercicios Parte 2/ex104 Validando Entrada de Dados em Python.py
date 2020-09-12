def leiaInt(a):
    while True:
        s = str(input(a))
        if s.isnumeric():
            s = int(s)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return s

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
