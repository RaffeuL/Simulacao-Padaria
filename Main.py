import simpy
from Cliente import Cliente
from Fila import fila_caixa
from Fila import fila_balcao


env = simpy.Environment()
recurso = simpy.Resource(env, capacity=1)
recurso2 = simpy.Resource(env, capacity=1)


cliente1 = Cliente("Carlos", 1, 0.30, 0.40)
cliente2 = Cliente("Jose", 1.10, 0.40, 1)
cliente3 = Cliente("Matilda", 1.15, 0.20, 0.20)
cliente4 = Cliente("Maria", 3, 0.30, 0.40)
cliente5 = Cliente("Fulano", 3, 0.30, 0.40)
cliente6 = Cliente("Ciclano", 3.10, 0.30, 0.40)

env.process(fila_caixa(env, recurso, cliente1))
env.process(fila_caixa(env, recurso, cliente2))
env.process(fila_caixa(env, recurso, cliente3))
env.process(fila_caixa(env, recurso, cliente4))
env.process(fila_caixa(env, recurso, cliente5))
env.process(fila_caixa(env, recurso, cliente6))


env.process(fila_balcao(env, recurso2, cliente1))
env.process(fila_balcao(env, recurso2, cliente2))
env.process(fila_balcao(env, recurso2, cliente3))
env.process(fila_balcao(env, recurso2, cliente4))
env.process(fila_balcao(env, recurso2, cliente5))
env.process(fila_balcao(env, recurso2, cliente6))

env.run()