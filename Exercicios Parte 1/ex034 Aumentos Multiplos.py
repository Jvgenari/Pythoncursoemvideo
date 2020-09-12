s = float(input('Digite seu salário: '))

if s > 1250.00:
    print('Seu sálario teve um aumento de R${:.2f} e foi para R${:.2f}'.format(((s/100) * 10), (s + (s/100) * 10)))
else:
    print('Seu sálario teve um aumento de R${:.2f} e foi para R${:.2f}'.format(((s/100) * 15), (s + (s/100) * 15)))


