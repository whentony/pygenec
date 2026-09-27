from numpy.random import random
from numpy import array
from .selecao import Selecao

class Roleta(Selecao):
    """
    Seleciona indivíduos para cruzamento usando
    roleta de selecão.
    
    Recebe como entrada:
    - populacao: Objeto criado a partir da classe Populacao.
    """
    
    def __init__(self, populacao):
        super(Roleta, self).__init__(populacao)
        
    def selecionar(self, fitness):
        """
        Retorna o índice do indivíduo selecionado
        usando roleta de seleção.
        """
        if fitness is None:
            fitness = self.populacao.avaliar()
        fmin = fitness.min()
        fitness = fitness - fmin
        total = fitness.sum()
        parada = total * (1.0 - random())
        parcial = 0
        i = 0
        while True:
            if i > fitness.size - 1:
                break
            parcial += fitness[i]
            if parcial >= parada:
                break
            i += 1
        return i - 1