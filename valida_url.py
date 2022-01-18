'''
Exemplos de URLs validas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs invalidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio

'''

##https://www.bytebank.com.br/cambio
import re

url ="https://www.bytebank.com.br/cambio"

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)
if not match:
    raise ValueError('A URL e invalida, por favor, insira uma correta')

print("A URL esta correta")