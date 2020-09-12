import math

ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
h = math.hypot(ca, co)

print('O comprimento da hipotenusa é {:.2f}'.format(h))
