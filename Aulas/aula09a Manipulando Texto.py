frase = 'Curso em Video Python'

#FATIAMENTO
print('\n### FATIAMENTO ###\n')
print(frase[3])
print(frase[:10])
print(frase[::2])
print(frase[9:21:2])  #Primeiro num = posição primeira letra, segundo final e terceiro pulo (2 em 2 no caso)


#ANÁLISE
print('\n### ANÁLISE ###\n')
print(len(frase))     #Tamanho da string

print(frase.count('o'))  #Contagem da letra 'o'

print(frase.count('o', 0, 13))    #Contagem letra 'o' do 0 ao 13

print(frase.find('deo'))   #Procura na string a posição da palavra

print('Curso' in frase)    #Diz True ou false se tem na string

print(frase.find('Android'))    #Quando não encontra, retorna -1

#TRANSFORMAÇÃO
print('\n### TRANSFORMAÇÃO ###\n')
print('Replace ----->', frase.replace('Python', 'Android'))   #Substitui uma palavra na string por outra, só funciona nesta instancia, precisa atribuir a frase para que possa realmente
                                                              #substituir. Ex: frase = frase.replace('Python', 'Android')

print('Upper ----->', frase.upper())  #Coloca todos os caracteres em maiusculo
print('Lower ----->', frase.lower())  #Coloca todos os caracteres em minusculo

print('Captalize ----->', frase.capitalize()) #Coloca todos os caracteres em minusculo menos o primeiro.

print('Title ----->', frase.title()) #Analisa quantas palavras a string tem e coloca a primeira letra de cada em maiusculo

print('\n### TRANSFORMAÇÃO DE ESPAÇO ###\n')
frase2 = '   Aprenda Python  '   #Frase com espaço no começo e no final (erro muito comum de usuario).

print('\n\nNormal ----->', frase2)
print('Strip ----->', frase2.strip()) #Remove os espaços inuteis do começo e do fim
print('rStrip ----->', frase2.rstrip()) #Remove os espaços so da direita
print('lStrip ----->', frase2.lstrip()) #Remove os espaços so da esquerda

#DIVISAO
print('\n### DIVISÃO ###\n')
dividido = frase.split()
print('Split ----->', dividido) #Ocorre uma divisão de palavras onde tiver espaço, colocando as em uma lista numerados em ordem 0~ etc EX:(prox linha)
print(dividido[0]) # Pega a 1ª palavra do dividido que é o [0]
print(dividido[2] [3]) # Pega a 3ª palavra do dividido que é o [2] e a sua 4ª letra que é o [3]
print('Join ----->', ' '.join(dividido)) #Junta a frase com o caracter de sua escolha


##  EXERCICIOS DO 22 AO 27  ##
