import pandas as pd
from Cliente import Cliente
lista_clientes = []
x = pd.read_excel("ListaClientes.xlsx", header=None, engine="openpyxl")
qtd_clientes = 50

for index in range(qtd_clientes):
    cliente_infos = x.iloc[[index]].values
    nome = cliente_infos[0][0]
    t_chegada_caixa = cliente_infos[0][1]
    t_atem_caixa = cliente_infos[0][2]
    t_atem_balcao = cliente_infos[0][3]
    lista_clientes.append(Cliente(nome, t_chegada_caixa, t_atem_caixa, t_atem_balcao))

def busca_clientes():
    return lista_clientes