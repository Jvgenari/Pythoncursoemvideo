matriz = [[], [], []]
somapar = maior = somatres = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f"Digite um valor para [{i},{j}]: "))
        matriz[i].append(n)
        if n % 2 == 0:
            somapar += n
        if j == 2:
            somatres += n
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
print('-=' * 30)
for b in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[b][c]:^5} ] ', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somatres}')
print(f'O maior valor da segunda linha é {maior}')
