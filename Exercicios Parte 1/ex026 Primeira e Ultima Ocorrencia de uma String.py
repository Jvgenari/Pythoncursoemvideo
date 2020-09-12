frase = input('Digite uma frase: ').strip().upper()
print('A letra "A" aparece {} vezes.\nAparece na posição {} primeiro.\nAparece na posição {} por ultimo.'
      .format(frase.count('A'), frase.find('A') + 1, frase.rfind('A') + 1))
