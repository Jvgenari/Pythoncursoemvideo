import moeda

p = float(input('Digite o preço da moeda: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10,True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13,True)}')
