class Cliente:
    def __init__(self, nome, cpf, sala):
        self.nome = nome
        self.cpf = cpf
        self.sala = sala
        self.poltrona = None

    def escolher_poltrona(self, clientes: list):
        for poltrona in self.sala.poltronas:
            if not any(cliente.poltrona == poltrona for cliente in clientes):
                self.poltrona = poltrona
                break
