r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
maior = 0
menor = 0
meio = 0
if r1 > r2:
    maior = r1
    menor = r2
else:
    maior = r2
    menor = r1

if maior < r3:
    maior = r3
    if r2>r1:
        meio = r2
    else:
        meio = r1
if menor > r3:
    menor = r3
    if r2>r1:
        maior = r2
        meio = r1
    else:
        maior = r1
        meio = r2

if maior >= meio + menor:
    print('Não é possivel formar um triângulo!')
else:
    print('É possivel formar um triângulo!')





