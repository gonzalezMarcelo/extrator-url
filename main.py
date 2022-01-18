url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"

#Sanitização da URL
url = url.strip()

#Validação da URL
if (url == ""):
    raise ValueError("A URL está vazia, preencha com valor correto")

#Separar as bases do parametro
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]

#Buscar um valor do parametro
parametro_busca = "moedaOrigem"
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find("&", indice_valor)
if (indice_e_comercial == -1):
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)