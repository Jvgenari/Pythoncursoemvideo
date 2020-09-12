num = []
pos = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    num.append(n)
    pos = len(num) - 1
    for i in range((len(num) - 1), -1, -1):
        if i-1 < 0:
            break
        if num[i] < num[i-1]:
            num.insert(i-1, n)
            num.pop(i+1)
            pos = (i-1)
    if pos == (len(num) - 1):
        print('Adicionado ao final da lista...')
    elif pos == 0:
        print('Adicionado no começo da lista...')
    else:
        print(f'Adicionado na posição {pos} da lista...')
print(f'Os valores digitados em ordem foram {num}')
