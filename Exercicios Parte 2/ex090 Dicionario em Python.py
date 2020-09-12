dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Média de {dic["nome"]}: '))
if dic['media'] < 7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Aprovado'
print('-=' * 30)
for k, i in dic.items():
    print(f'  - {k} é igual a {i}')
