def leiaInt(a):
    while True:
        try:
            s = int(input(a))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return s


def leiaFloat(a):
    while True:
        try:
            s = float(input(a))
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        else:
            return s
i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
