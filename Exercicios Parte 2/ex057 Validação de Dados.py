sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Sexo incorreto!\nDigite M ou F: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
