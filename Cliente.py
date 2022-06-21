class Cliente:
    def __init__(self, nome, t_chegada_caixa, t_atem_caixa, t_atem_balcao):
        self.nome = nome
        self.t_chegada_caixa = t_chegada_caixa
        self.t_atem_caixa = t_atem_caixa
        self.t_chegada_balcao = t_chegada_caixa + t_atem_caixa + 0.01
        self.t_atem_balcao = t_atem_balcao