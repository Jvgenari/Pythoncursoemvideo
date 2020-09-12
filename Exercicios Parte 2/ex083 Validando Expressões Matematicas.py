exp = []
string = str(input('Digite a expressão: '))

for simb in string:
    if simb == '(':
        exp.append('(')
    elif simb == ')':
        if len(exp) > 0:
            exp.pop()
        else:
            exp.append(')')
            break
if len(exp) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada!')
