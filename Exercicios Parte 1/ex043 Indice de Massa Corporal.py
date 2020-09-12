peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

imc = peso / altura**2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Parabéns, você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Cuidado, você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Cuidado, você está com OBESIDADE!')
elif imc >= 40:
    print('Cuidado, você está com OBESIDADE MÓRBIDA!')
