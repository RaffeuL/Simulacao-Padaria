def fila_caixa(env, recurso, cliente, chegada):
    yield env.timeout(chegada)
    with recurso.request() as req:
        yield req
        print(cliente.nome, 'atendida em ', env.now)
        yield env.timeout(0.40)

def fila_balcao(env, recurso, cliente, chegada):
    yield env.timeout(chegada)
    with recurso.request() as req:
        yield req
        print(cliente.nome, 'atendida em ', env.now)
        yield env.timeout(1)