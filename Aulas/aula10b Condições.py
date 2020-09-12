n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2
print('A sua media foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('Sua media foi ruim! Estude mais!')

print('Você Passou!' if m>= 6 else 'REPROVADO!')

#Exercicios 28 ao 35!
