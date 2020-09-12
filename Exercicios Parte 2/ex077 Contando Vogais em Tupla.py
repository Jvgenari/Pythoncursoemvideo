palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for z in i:
        if z in 'aeiou':
            print(f'{z} ', end='')
