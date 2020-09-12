n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('O aluno ficou com a média {:.1f} e foi REPROVADO!'.format(media))
elif 5 <= media < 7:
    print('O aluno ficou com a média {:.1f} e está de RECUPERAÇÃO!'.format(media))
else:
    print('O aluno ficou com a média {:.1f} e foi APROVADO!'.format(media))