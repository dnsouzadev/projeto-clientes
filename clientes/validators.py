import re
from validate_docbr import CPF

cpf = CPF()

def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11 and cpf.validate(numero_cpf)

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
