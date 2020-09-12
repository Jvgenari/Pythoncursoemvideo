def notas(* n, sit=False):
    '''
    -> Função notas é para analizar notas e situações de vários alunos.
    :param n: Uma ou mais notas do alunos
    :param sit: Valor opcional, se deve ou não mostar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    notas = {}
    maior = menor = media = 0
    total = len(n)
    for c in range(0, len(n)):
        media += n[c]
        if c == 0:
            menor = n[c]
            maior = n[c]
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
    '''''
    Tem como ser assim também: (menos trabalho)
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['média'] = sum(n)/len(n)
    '''''

    media /= total
    notas['total'] = total
    notas['maior'] = maior
    notas['menor'] = menor
    notas['média'] = media
    if sit == True:
        if media < 5:
            notas['situação'] = 'RUIM'
        elif media >= 5:
            notas['situação'] = 'RAZOAVEL'
        elif media >= 7:
            notas['situação'] = 'BOA'
    return notas


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
