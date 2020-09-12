num = [2, 5, 9, 1]   # LISTA
num[2] = 3          # Substituiu o valor na posição 2
num.append(7)       # Adicionou o valor 7 no final da lista
num.sort(reverse=True)   # Ordena a lista em ordem crescente, reverse=True coloca em descrescente
num.insert(2, 0)      # Inseriu na posição 2 o valor 0, jogando os valores para frente.
num.pop()        # () remove o ultimo.
num.pop(2)      # remove na posição 2
num.remove(2)   # remove por conteúdo, no caso o número 2

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):     # For pega a chave (c) e o valor (v) de valores com a função enumerate
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

valores2 = []
# ----------------------------------------------------------------------------------------------------
for cont in range(0, 5):            # Digitando pelo teclado uma lista
    valores2.append(int(input('Digite um valor: ')))

print(valores2)
# ----------------------------------------------------------------------------------------------------
a = [2, 3, 4, 7]                      # Criei uma lista a e atribui [a] lista [b] e ao mudar o valor da posição 2 da lista [b] o da lista [a] também muda,
                                      # pois assim vc cria uma ligação entre elas
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# ----------------------------------------------------------------------------------------------------
a = [2, 3, 4, 7]                      # Adicionando o [:] vc cria uma cópia da lista [a] com a lista [b], então o valor atribuido so muda para a lista [b]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
