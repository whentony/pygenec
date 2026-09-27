from numpy.random import randint
from numpy import array

from .mutacao import Mutacao

class DuplaTroca(Mutacao):
    """
    Mutação dupla troca
    
    Entrada:
        pmut - probabilidade de ocorrer a mutação em um indivíduo.

    Args:
        Mutacao (_type_): _description_
    """

    def __init__(self, pmut):
        super(DuplaTroca, self).__init__(pmut)

    def mutacao(self):
        """
        Alteração genética de membros da população usando mutação dupla troca.
        """
        nmut = self.selecao()
        if len(nmut) > 0:
            gen1 = array([randint(0, self.ngen) for _ in range(len(nmut))], dtype=int)
            gen2 = array([randint(0, self.ngen) for _ in range(len(nmut))], dtype=int)
            self.populacao[nmut, gen1], self.populacao[nmut, gen2] = self.populacao[nmut, gen2], self.populacao[nmut, gen1]