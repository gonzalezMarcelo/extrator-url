endereco = "Rua São João, 110, apartamento 900, Itaboraí, Rio de Janeiro, RJ, Brasil, 22021000"

import re #Regular Expressions

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
else:
    print("voce e um corno que nao botou o cep certo")
