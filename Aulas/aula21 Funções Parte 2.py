print('-=' * 50)
print('##########################   INTERACTIVE HELP   #######################')
print('-=' * 50)
### 1ª maneira: Abre o console do pycharm e escreve 'help()', agora você pode pegar o manual de qualquer função, comando, biblioteca, etc... // quit para sair
### 2ª maneira:
help(print)

print('-=' * 50)
print('##########################   DOCSTRINGS   #######################')
print('-=' * 50)
### Cria um manual para funções novas criadas por você ou por outros dai podendo utilizar o help(nome da função)###
## EX: Abre três pares de " dentro da função e o pycharm já cria um mini help e você descreve o que a função faz, depois pode chamar no help(contador)
def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param inicio: início da contagem
    :param fim: final da contagem
    :param passo: passo da contagem
    :return: sem retorno
    """
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo > 0:
        if inicio < fim:
            while inicio <= fim:
                print(f'{inicio} ', end='')
                inicio += passo
            print('FIM!')
        else:
            while inicio >= fim:
                print(f'{inicio} ', end='')
                inicio -= passo
            print('FIM!')


contador(1, 10, 1)
help(contador)

print('-=' * 50)
print('##########################   PARÂMETROS OPCIONAIS   #######################')
print('-=' * 50)
### Caso crie uma função que recebe 3 variáveis e na hora da chamada, só colocar 2 variáveis, a função não funciona. Para poder funcionar nessa situação,
# você pode criar parâmetros opcionais, colocando valores na definição da função. ex: def soma(a=0, b=0, c=0)
#ex:
def somar(a, b, c):
    s = a + b + c
    print(f'A soma vale {s}')

def somar2(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)  ## funcionaria
#somar(2, 8)     ## não funcionaria, dai coloca os parametros opcionais lá na função ex: a=0, b=0, c=0 como no somar2
somar2(2, 5)
somar2()

print('-=' * 50)
print('##########################   ESCOPO DE VARIÁVEIS   #######################')
print('-=' * 50)
### Variaveis declaradas em funções são locais, existem somente na área da função, já as globais, em qualquer área.
def funçao():
    n1 = 4                    # Cria uma variavel n1 local
    x = 9                     # Cria uma variavel x local
    global n3                 # Faz utilizar o n3 da função principal, não criando uma local
    n3 = 20                   # Muda o valor da n3 GLOBAL para 20
    print(f'N1 local vale {n1}')
    print(f'Puxando o n2 global valendo {n2}')
    print(f'X local vale {x}')


n1 = 2
n2 = 5
n3 = 9
funçao()
print(f'N1 global vale {n1}')
print(f'N2 global vale {n2}')
#print(f'X local não pega {x}')     {Não funcionaria}
print(f'N3 global vale {n3}')

print('-=' * 50)
print('##########################   RETORNO DE VALORES   #######################')
print('-=' * 50)
## Faz a função retornar um valor
def somar3(a=0, b=0, c=0):
    s = a + b + c
    return s  # retorna o valor s


r1 = somar3(3, 2, 5)   # r1 para receber o valor da função
r2 = somar3(2, 2)   # r2 para receber o valor da função
r3 = somar3(6)   # r3 para receber o valor da função
print(f'Meus calculos deram {r1}, {r2}, {r3}')

print('-=' * 50)
print('##########################   PARTE PRÁTICA   #######################')
print('-=' * 50)

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *=c
    return f


n = int(input('Digite um número: '))
f = fatorial(n)
print(f'O fatorial de {n} é igual a {f}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')