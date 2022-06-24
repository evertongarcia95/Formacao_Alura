import re  # Regular Expression -- RegEx
endereço_test = "Rua silva de camargo lima, n° 81, apartamento 22A bloco 27, vila Padre Anchieta, campinas, sp 30134-800 "


# 5 digitos + hifen (opicional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereço_test)   # match
if busca:
    cep = busca.group()
    print(cep)
