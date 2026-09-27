from numpy.random import randint, random
from numpy import array

class Mutacao:
    """
    Classe base para mutação de indivíduos.
    
    Entrada:
        pmut - probabilidade de ocorrer a mutação em um indivíduo.
    """
    def __init__(self, pmut):
        self.pmut = pmut
        self._populacao = None 
        self.npop = None
        self.ngen = None
        
    def _set_populacao(self, populacao):
        self._populacao = populacao
        self.npop = self._populacao.shape[0]
        self.ngen = self._populacao.shape[1]
    
    def _get_populacao(self):
        return self._populacao
    
    def selecao(self):
        nmut = array([i for i in range(self.npop) if random() < self.pmut])
        return nmut
    
    def mutacao(self):
        raise NotImplementedError("O método mutacao deve ser implementado nas subclasses.")
    
    populacao = property(_get_populacao, _set_populacao)