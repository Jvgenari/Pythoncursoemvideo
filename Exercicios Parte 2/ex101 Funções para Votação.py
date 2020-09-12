from datetime import date


def voto(ano):
    if ano < 16:
        s = 'VOTO NEGADO.'
    elif ano < 18 or ano > 70:
        s = 'VOTO OPCIONAL.'
    else:
        s = 'VOTO OBRIGATÓRIO.'
#   Da para fazer assim tbm, EX:
#   if idade < 16:
#       return f'Com {idade} anos: NÃO VOTA.'

    return s


year = int(input('Em que ano você nasceu? '))
idade = date.today().year - year
v = voto(idade)
print(f'Com {idade} anos: {v}')
