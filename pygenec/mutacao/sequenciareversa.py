from numpy.random import randint
from numpy import array

from .mutacao import Mutacao

class SequenciaReversa(Mutacao):
    """
    Mutação sequência reversa
    
    Entrada:
        pmut - probabilidade de ocorrer a mutação em um indivíduo.

    Args:
        Mutacao (_type_): _description_
    """

    def __init__(self, pmut):
        super(SequenciaReversa, self).__init__(pmut)

    def mutacao(self):
        """
        Alteração genética de membros da população usando mutação sequência reversa.
        """
        nmut = self.selecao()
        if len(nmut) > 0:
            for k in nmut:
                i = randint(0, self.ngen)
                j = randint(0, self.ngen)
                while i == j:
                    j = randint(0, self.ngen)
                if i > j:
                    i, j = j, i
                self.populacao[k, i:j] = self.populacao[k, i:j][::-1]