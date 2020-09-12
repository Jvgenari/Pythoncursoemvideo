def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

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


def menu(lista):
    while True:
        cabeçalho('MENU PRINCIPAL')
        c = 1
        for item in lista:
            print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
            c+=1
        print(linha())
        n = leiaInt('\033[32mSua Opção: \033[m')
        return n



def cadastar():
    while True:
        try:
            s = str(input('Nome: '))
            Idade = int(input('Idade: '))
        except:
            print('\033[0;31mERRO: por favor, digite um número válido.\033[m')
        try:
            Idade = int(input('Idade: '))
        except:
            print('\033[0;31mERRO: por favor, digite um número válido.\033[m')

def listar(lista):
    lista = []
    for i, v in enumerate(lista):
        print()


