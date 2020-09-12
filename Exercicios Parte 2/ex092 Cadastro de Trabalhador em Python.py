from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Carteira de Trabbalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - ano) + 35
print('-=' * 30)
for i, v in pessoa.items():
    print(f'{i} tem o valor {v}')
