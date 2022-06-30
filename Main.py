from Padaria import Padaria
from Clientes import busca_clientes
import simpy
import matplotlib.pyplot as plt

def simula_Padaria(qtd_caixas: int , qtd_balconistas: int, clientes=''):
    env = simpy.Environment()
    caixas = simpy.Resource(env, capacity=qtd_caixas)
    balconistas = simpy.Resource(env, capacity=qtd_balconistas)
    p = Padaria(env, caixas, balconistas)

    for cliente in clientes:
        env.process(p.atender(cliente))
    
    env.run()

def grafico_tempo_espera(clientes):
    index_cliente = 0
    tempos = []
    nomes = []
    for cliente in clientes:
        index_cliente += 1
        nomes.append(index_cliente)
        tempos.append(cliente.t_espera_total)

    fig, ax = plt.subplots()
    ax.bar(nomes, tempos)
    plt.show()

clientes = busca_clientes()
simula_Padaria(1, 1, clientes)
grafico_tempo_espera(clientes)