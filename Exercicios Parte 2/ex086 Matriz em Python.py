matriz = [[], [], []]
matriz = [[] * 2]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Digite um valor para [{i},{j}]: ")))
print('-=' * 30)

for b in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[b][c]:^5} ] ', end='')
    print()
