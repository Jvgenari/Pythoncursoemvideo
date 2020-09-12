v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual seu salario? R$'))
a = float(input('Quantos anos ira pagar? '))
p = v / (a * 12)

if ((s/100) * 30) <= p:
    print('O valor da prestação será de R${:.2f}, infelizmente você não pode financiar esta casa.\nEmprestimo NEGADO!'.format(p))
else:
    print('O valor da prestação será de R${:.2f}.Emprestimo pode ser CONCEDIDO!'.format(p))
