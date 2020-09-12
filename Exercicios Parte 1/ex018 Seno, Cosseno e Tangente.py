from math import sin, cos, tan, radians
a = int(input('Digite o angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('Do angulo {:.2f} você tem\n{:.2f} de seno\n{:.2f} de cosseno\n{:.2f} de tangente'.format(a, s, c, t))
