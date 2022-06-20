from msilib.schema import Class


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.chegada_balcao = 0