from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    for c in num:
        print(f'{c} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo')

    m = 0
    for c in range(0, len(num)):
        if num[c] > m:
            m = num[c]
    print(f'O maior valor informado foi {m}')


maior(2, 4, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
