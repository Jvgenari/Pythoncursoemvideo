n = int(input('Escreva um número inteiro: '))
print('BASE DE CONVERSÃO\n[ 1 ] - BINÁRIO\n[ 2 ] - OCTAL\n[ 3 ] - HEXADECIMAL')
c = int(input('Sua Opção: '))

if c == 1:
    print('{} convertido para BINÁRIO é igual á {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('{} convertido para OCTAL é igual á {}'.format(n, oct(n)[2:]))
elif c ==3:
    print('{} convertido para HEXADECIMAL é igual á {}'.format(n, hex(n)[2:]))
else:
    print('Número inválido!')



