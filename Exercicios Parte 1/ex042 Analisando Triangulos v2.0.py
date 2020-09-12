r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triângulo com essas retas!')
    if r1 == r2 == r3:
        print('O triângulo formado é um EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é um ESCALENO!')
    else:
        print('O triângulo formado é um ISÓSCELES!')
else:
    print('Não e possível formar um triângulo com essas retas!')
