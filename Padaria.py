class Padaria:
    def __init__(self, env,caixas, balconistas):
        self.env = env
        self.caixas = caixas
        self.balconistas = balconistas
        self.cliente = ''

    def atender(self, cliente):
        yield self.env.timeout(cliente.t_chegada_caixa)
        print(cliente.nome, 'chegou no CAIXA em', self.env.now)
        with self.caixas.request() as caixa:
            yield caixa
            print(cliente.nome, 'iniciou atendimento no CAIXA em', self.env.now)
            yield self.env.timeout(cliente.t_atem_caixa)
            print(cliente.nome, 'saiu do CAIXA em', self.env.now)
            self.env.process(self.atender_balcao(cliente))

    def atender_balcao(self, cliente):
        print(cliente.nome, 'chegou no BALCAO em', self.env.now)
        with self.balconistas.request() as balconista:
            yield balconista
            print(cliente.nome, 'inicou atendimento no BALCAO em', self.env.now)
            yield self.env.timeout(cliente.t_atem_balcao)
            print(cliente.nome, 'saiu do BALCAO em', self.env.now)