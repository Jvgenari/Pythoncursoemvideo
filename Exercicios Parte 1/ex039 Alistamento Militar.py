from datetime import date
import math
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
e = idade - 18
if idade < 18:
    se = date.today().year + e
    e = e * -1
    print('Quem nasceu em {} tem {} anos em {}.\nAinda faltam {} anos para o alistamento.\nSeu alistamento será em {}'.format(ano, idade, date.today().year, e, se))
elif idade > 18:
    se = date.today().year - e
    print('Quem nasceu em {} tem {} anos em {}.\nJá deveria ter se alistado há {} anos.\nSeu alistamento foi em {}'.format(ano, idade, date.today().year, e, se))
else:
    print('Quem nasceu em {} tem {} anos em {}.\nVocê tem que se alistar IMEDIATAMENTE!'.format(ano, idade, date.today().year))
