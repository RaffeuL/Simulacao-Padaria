class Cliente:
    def __init__(self, nome, t_chegada_caixa, t_atem_caixa, t_atem_balcao):
        self.nome = nome
        self.t_chegada_caixa = t_chegada_caixa
        self.t_atem_caixa = t_atem_caixa
        self.t_atem_balcao = t_atem_balcao
        self.t_espera_total = 0