import random
from poltrona import Poltrona
from filme import Filme

class Sala:
    def __init__(self, numero):
        self.numero = numero
        self.poltronas = self.criar_poltronas()
        self.filme = self.sortear_filme()

    def criar_poltronas(self):
        poltronas = []
        cores = ['Vermelha', 'Azul', 'Verde', 'Amarela', 'Preta']
        for i in range(1, 6):
            cor = random.choice(cores)
            poltrona = Poltrona(i, cor)
            poltronas.append(poltrona)
        return poltronas

    def sortear_filme(self):
        return random.choice(Filme.lista_filmes())