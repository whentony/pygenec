from numpy.random import randint
from numpy import array

from .mutacao import Mutacao

class Flip(Mutacao):
    """
    Mutação flip
    
    Entrada:
        pmut - probabilidade de ocorrer a mutação em um indivíduo.

    Args:
        Mutacao (_type_): _description_
    """
    
    def __init__(self, pmut):
        super(Flip, self).__init__(pmut)
        
    def mutacao(self):
        """
        Alteração genética de membros da população usando mutação flip.
        """
        nmut = self.selecao()
        genflip = array([randint(0, self.ngen - 1) for _ in range(len(nmut))])
        self.populacao[nmut, genflip] = 1 - self.populacao[nmut, genflip]