frase = str(input('Digite uma frase qualquer: ')).strip().upper()
frasej = frase.replace(' ', '')
t = len(frasej)
frase2 = ''
#frase2 = frasej[::-1]  --> PEGA A FRASE AO CONTRÁRIO, NÃO PRECISANDO DO FOR ABAIXO!
for i in range(t-1, -1, -1):
    frase2 += frasej[i]
print('O inverso de {} é {}'.format(frasej, frase2))
if frasej == frase2:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
