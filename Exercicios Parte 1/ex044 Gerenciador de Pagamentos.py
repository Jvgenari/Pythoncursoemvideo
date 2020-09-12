compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n[ 1 ] á vista dinheiro/chque\n[ 2 ] á vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opçao = int(input('Qual a opção? '))

if opçao == 1:
    total = compras - ((compras/100) * 10)
elif opçao == 2:
    total = compras - ((compras/100) * 5)
elif opçao == 3:
    total = compras
    print('Sua compra será parcelada em 2x de {:.2f}'.format(total/2))
elif opçao == 4:
    opçao2 = int(input('Quantas parcelas? '))
    total = compras + ((compras/100)*20)
    parcelas = total / opçao2
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(opçao2, parcelas))
else:
    total = compras
    print('Opção inválida!')

print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(compras, total))

