class Cliente:
    def __init__(self, env, nome, t_chegada_caixa, t_atem_caixa, t_atem_balcao):
        self.env = env
        self.nome = nome
        self.t_chegada_caixa = t_chegada_caixa
        self.t_atem_caixa = t_atem_caixa
        self.t_atem_balcao = t_atem_balcao