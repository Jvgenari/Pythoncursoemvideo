soma = 0
i = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        i += 1
        soma += n
print('A soma de todos os {} valores solicitados é {}'.format(i, soma))
