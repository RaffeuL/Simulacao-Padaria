from Padaria import Padaria
from Clientes import busca_clientes
import simpy

def simula_Padaria(qtd_caixas: int , qtd_balconistas: int, clientes=''):
    env = simpy.Environment()
    caixas = simpy.Resource(env, capacity=qtd_caixas)
    balconistas = simpy.Resource(env, capacity=qtd_balconistas)
    
    #(env, tempo de chegada do cliente no caixa, tempo que ele demorou no caixa, tempo que ele demorou no balcão)

    p = Padaria(env, caixas, balconistas)

    for cliente in clientes:
        env.process(p.atender(cliente))


    env.run()


clientes = busca_clientes()
simula_Padaria(1, 1, clientes)
