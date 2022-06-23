from Padaria import Padaria
from Cliente import Cliente
import simpy

def simula_Padaria(qtd_caixas: int , qtd_balconistas: int, clientes=''):
    env = simpy.Environment()
    caixas = simpy.Resource(env, capacity=qtd_caixas)
    balconistas = simpy.Resource(env, capacity=qtd_balconistas)
    
    #(env, tempo de chegada do cliente no caixa, tempo que ele demorou no caixa, tempo que ele demorou no balcão)
    c1 = Cliente(env, "Carlos", 1, 0.30, 0.40)
    c2 = Cliente(env, "Jose", 1.10, 0.40, 1)
    c3 = Cliente(env, "Matilda", 1.15, 0.20, 0.20)

    p = Padaria(env, caixas, balconistas)

    env.process(p.atender(c1))
    env.process(p.atender(c2))
    env.process(p.atender(c3))

    env.run()


simula_Padaria(2, 1)
