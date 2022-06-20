import simpy
from Cliente import Cliente
from Fila import fila_caixa
from Fila import fila_balcao


env = simpy.Environment()
recurso = simpy.Resource(env, capacity=1)
recurso2 = simpy.Resource(env, capacity=1)


cliente1 = Cliente("Carlos")
cliente2 = Cliente("Jose")
cliente3 = Cliente("Matilda")
cliente4 = Cliente("Maria")
cliente5 = Cliente("Fulano")
cliente6 = Cliente("Ciclano")

env.process(fila_caixa(env, recurso, cliente1, 0))
env.process(fila_caixa(env, recurso, cliente2, 0.30))
env.process(fila_caixa(env, recurso, cliente3, 2))
env.process(fila_caixa(env, recurso, cliente4, 3))
env.process(fila_caixa(env, recurso, cliente5, 3))
env.process(fila_caixa(env, recurso, cliente6, 3.30))

env.process(fila_balcao(env, recurso2, cliente1, cliente1.chegada_balcao))
env.process(fila_balcao(env, recurso2, cliente2, cliente2.chegada_balcao))
env.process(fila_balcao(env, recurso2, cliente3, cliente3.chegada_balcao))
env.process(fila_balcao(env, recurso2, cliente4, cliente4.chegada_balcao))
env.process(fila_balcao(env, recurso2, cliente5, cliente5.chegada_balcao))
env.process(fila_balcao(env, recurso2, cliente6, cliente6.chegada_balcao))

env.run()