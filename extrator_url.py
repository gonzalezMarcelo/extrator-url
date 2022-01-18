import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url) #erro aq
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str: #erro aq
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL esta vazia, preencha com valor correto")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL e invalida, por favor, insira uma correta')

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if (indice_e_comercial == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + self.get_url_base() + '\n' + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url

bytebank = ExtratorURL("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")
bytebank_2 = ExtratorURL("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")
moeda_origem = bytebank.get_valor_parametro("moedaOrigem")
moeda_destino = bytebank.get_valor_parametro("moedaDestino")
quantidade = bytebank.get_valor_parametro("quantidade")
valor_dolar  = 5.57

if (moeda_origem == 'dolar' and moeda_destino == 'real'):
    valor_conversao = int(quantidade) / valor_dolar
    print("O valor da sua conversao e {} reais".format(str(valor_conversao)))
elif (moeda_origem == 'real' and moeda_destino == 'dolar'):
    valor_conversao = int(quantidade) * valor_dolar
    print("O valor da sua conversao e {} dolar".format(str(valor_conversao)))
else:
    print("O cambio de {} para {} nao esta disponivel".format(moeda_origem, moeda_destino))

print(len(bytebank))
print(bytebank)
print(bytebank == bytebank_2)
print(quantidade)

print(id(bytebank))
print(id(bytebank_2))

print(bytebank is bytebank_2) #compara as id dos objetos --> sao diferentes por isso false