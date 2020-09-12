nome = input('Digite seu nome: ')

print('Nome Maiusculo: ', nome.upper())
print('Nome Minusculo: ',nome.lower())
nse = nome.split()
nse = ''.join(nse)
v = len(nse.strip())
print('Quantas letras possui sem espaço: ', v)
v2 = nome.split()
v2 = v2[0]
print('Quantas letras possui o primeiro nome: ', len(v2))


