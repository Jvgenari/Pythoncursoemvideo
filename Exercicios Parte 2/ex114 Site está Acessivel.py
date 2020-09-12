import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[0;31mDeu erro! Não consegui acessar o site!\033[m')
else:
    print('\033[0;32mConsegui acessar o site!\033[m')
