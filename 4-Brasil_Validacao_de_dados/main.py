from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
import re
from datetime import date, datetime, timedelta
from acesso_cep import BuscaEndereco
import requests

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"


cpf_um = Documento.cria_documento(exemplo_cpf)
print(cpf_um)

cnpj_um = Documento.cria_documento(exemplo_cnpj)
print(cnpj_um)

telefone1 = "551982328196"
telefone_exemplo = TelefonesBr(telefone1)

print(telefone_exemplo)

cadastro = DatasBr()
print(cadastro)
print(cadastro.dia_semana())
print(cadastro.mes_cadastro())


cadastro = DatasBr()
print(cadastro.tempo_cadastro())

cep = "01001000"
exemplo_cep = BuscaEndereco(cep)

bairro, localidade, uf = exemplo_cep.acesse_via_cep()
print( bairro, localidade, uf)
