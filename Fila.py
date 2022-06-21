def fila_caixa(env, recurso, cliente):
    yield env.timeout(cliente.t_chegada_caixa)
    with recurso.request() as req:
        yield req
        print(cliente.nome, 'chegou no CAIXA em: ', env.now)
        yield env.timeout(cliente.t_atem_caixa)
        print(cliente.nome, 'Terminou o atendimento no CAIXA em: ', env.now)
        cliente.t_chegada_balcao = env.now
#Ajeitar essa função aqui
def fila_balcao(env, recurso, cliente):
    yield env.timeout(cliente.t_chegada_balcao)
    with recurso.request() as req:
        yield req
        print(cliente.nome, 'chegou no BALCAO em: ', env.now)
        yield env.timeout(cliente.t_atem_balcao)
        print(cliente.nome, 'Terminou o atendimento no BALCAO em: ', env.now)