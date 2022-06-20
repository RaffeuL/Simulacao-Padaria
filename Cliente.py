from msilib.schema import Class


class Cliente:
    def __init__(self, env, tempo_caixa, tempo_balcão, nome):
        self.env = env

        self.caixa_disponivel = self.env.event()
        #self.balcao_disponivel = self.env.event()

        self.tempo_de_caixa = tempo_caixa
        self.tempo_de_balcao = tempo_balcão
        self.nome = nome
        
        self.env.process(self.chegou_cliente())
        self.env.process(self.chegou_caixa())

        #self.env.process(self.chegou_cliente_balcao())
        #self.env.process(self.chegou_balconista())

    def chegou_cliente(self):
        yield self.caixa_disponivel
        print(self.nome, "foi atendido(a) no Caixa ", self.env.now)
        
    def chegou_caixa(self):
        yield self.env.timeout(0.30)
        self.caixa_disponivel.succeed()

    def chegou_cliente_balcao(self):
        yield self.balcao_disponivel
        print(self.nome, " foi atendido(a) no Balcao ", self.env.now)

    def chegou_balconista(self):
        yield self.env.timeout(self.tempo_de_balcao)
        self.balcao_disponivel.succeed()

'''
    def run(self):
        while True:
            yield self.caixa_disponivel
            self.env.timeout(self.tempo_de_caixa)
            print("Cliente foi atendido no Caixa ", self.env.now)
            
            yield self.env.timeout(self.tempo_de_balcao)
            print("Cliente foi atendido no Balcao ", self.env.now)
'''
