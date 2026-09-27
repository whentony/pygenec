from numpy.random import random
from numpy import array, argsort

from .selecao import Selecao

class Classificacao(Selecao):
    """
    Seleciona indivíduos para cruzamento usando
    Classificação.
    Recebe como entrada;
        populacao - A população de indivíduos a ser selecionada.
    """
    
    def __init__(self, populacao):
        super(Classificacao, self).__init__(populacao)
        
    def selecionar(self, fitness):
        """Roleta de seleção baseada em classificação"""
        if fitness is None:
           fitness = self.populacao.avaliar()
        classificacao = argsort(fitness) + 1
        total = classificacao.sum()
        parada = total * random()
        parcial = 0
        i = 0
        while True:
            if i > fitness.size - 1:
                break
            parcial += classificacao[i]
            if parcial >= parada:
                break
            i += 1
        return i - 1