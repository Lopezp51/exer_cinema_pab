import random
from poltrona import Poltrona
from filme import Filme

class Sala:
    def __init__(self, numero: int):
        self.numero = numero
        self.poltronas = self.criar_poltronas()
        self.filme = self.sortear_filme()

    def criar_poltronas(self):
        poltronas = []
        cores = ['Vermelha', 'Azul', 'Verde', 'Amarela', 'Preta']
        random.shuffle(cores) 
        for numero_poltrona in range(1, 6):
            cor = cores.pop() 
            poltrona = Poltrona(numero_poltrona, cor)
            poltronas.append(poltrona)
        return poltronas

    def sortear_filme(self):
        filme_sorteado = random.choice(Filme.lista_filmes())
        return filme_sorteado