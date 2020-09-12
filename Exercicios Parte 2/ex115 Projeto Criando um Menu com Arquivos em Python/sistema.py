from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo econtrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    n = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if n == 1:
        lerArquivo(arq)
    elif n ==2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    elif n == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[031mERRO! Digite uma opção válida!\033[m')
    sleep(1)

