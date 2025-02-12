class Cliente:
    def __init__(self, nome, cpf, sala):
        self.nome = nome
        self.cpf = cpf
        self.sala = sala
        self.poltrona = None

    def escolher_poltrona(self, clientes):
        for poltrona in self.sala.poltronas:
            if poltrona not in [c.poltrona for c in clientes]:
                self.poltrona = poltrona
                break
