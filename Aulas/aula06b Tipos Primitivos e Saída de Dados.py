n = input('Digite algo: ')

#print('O tipo dele é {}, {} para numérico, {} para letra, {} para letra minúscula, {} para letra maiuscula'.format(type(n), n.isnumeric(), n.isalpha(), n.islower(), n.isupper()))

print(f'O tipo dele é: {type(n)}\n {n.isnumeric()} para numérico\n {n.isalpha()} para letra\n {n.islower()} para letra minúscula\n {n.isupper()} para letra maiuscula')

