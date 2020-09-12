pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}    # declarando um dicionario
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # print no dicionario (especifico precisa de aspas duplas["])
print(pessoas.keys())# Mostra somente as chaves.
print(pessoas.values())# Mostra apenas os valores.
print(pessoas.items())# Mostra as chaves e os valores
del pessoas['sexo'] # Apagou a chave sexo e seu valor.
pessoas['nome'] = 'Leandro' # Mudou o valor da chave nome para Leandro
pessoas['peso'] = 98.5 # Adicionou uma nova chave peso com valor 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-=' * 30)

brasil = []                                               # Declarei uma lista e
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}         # 2 dicionario e
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}              #  //
brasil.append(estado1)                                    # adicionei na lista.
brasil.append(estado2)
print(brasil)               # mostra os dois elementos(dicionarios) da lista.
print(brasil[0])    # Mostra o elemento 0 da lista, no caso o dicionario estado1
print(brasil[0]['uf']) # mostra somente o 'uf' do dicionario estado1
print('-=' * 30)
#  **************************        APPEND EM LISTA                              **********************
estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())      # Somente funcionará se atribuir a função .copy
print(brasil)
