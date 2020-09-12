tabela = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Ceará SC', 'Corinthias', 'Coritiba', 'Flamengo',
          'Fluminense', 'Fortaleza', 'Goias', 'Gremio', 'Internacional', 'Palmeiras')

print(f'Os 5 primeiros time são {tabela[0:5]}')
print('-=' * 10)
print(f'Os 4 últimos são{tabela[-4:]}')
print('-=' * 10)
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print('-=' * 10)
n = tabela.index('Bahia')
print(f'O Bahia está na posição {n}')