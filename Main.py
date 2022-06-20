import simpy
from Cliente import Cliente

def fila(env, recurso, pessoa, chegada):
    yield env.timeout(chegada)
    with recurso.request() as req:
        yield req
        print(pessoa, 'atendida em ', env.now)
        yield env.timeout(0.40)

env = simpy.Environment()
recurso = simpy.Resource(env, capacity=1)
env.process(fila(env, recurso, 'Carlos', 0))
env.process(fila(env, recurso, 'Maria', 0.30))
env.process(fila(env, recurso, 'Joao', 2))
env.process(fila(env, recurso, 'Amendoin', 3))
env.process(fila(env, recurso, 'Anya', 3))
env.process(fila(env, recurso, 'Bolsonaro', 3.30))

env.run()


'''
cliente1 = Cliente(env, 0.10, 0.40, "Carlos")
cliente2 = Cliente(env, 0.20, 0.40, "Jose")
cliente3 = Cliente(env, 0.50, 1, "Matilda")
cliente4 = Cliente(env, 1.20, 0.20, "Maria")
cliente5 = Cliente(env, 1.40, 0.40, "Fulano")
cliente6 = Cliente(env, 3, 0.30, "Ciclano")
'''