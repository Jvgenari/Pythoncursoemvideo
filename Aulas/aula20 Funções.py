def lin ():                                       # Cria uma função de fazer linhas
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def contador(* num):                              #CRIA UMA TUPLA
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


lin()                                             # Chamei a função
print('   CURSO EM VIDEO   ')
lin()


soma(2, 4)                                        # Chamei a função soma com 2 e 4
soma(b= 4, a =5)                                  # Posso definir todas as variaveis (só funciona se for todas).

contador(2, 1, 7)                                 #Chamei a função contador criando uma tupla.
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0 , 2]
dobra(valores)
print(valores)

