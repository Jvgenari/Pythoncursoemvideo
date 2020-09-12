p = float(input('Qual o preço do produto? '))

d: float
v: float
d = (p/100) * 5
v = p - d
print('O produto que custava {:.2f} vale {:.2f} com 5% de desconto.'.format(p, v))

