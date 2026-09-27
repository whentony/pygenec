from numpy.random import choice
from numpy import array, where

from .selecao import Selecao

class Torneio(Selecao):
    """
    Seleciona indivíduos para cruzamento usando
    Torneio.
    Recebe como entrada;
        populacao - A população de indivíduos a ser selecionada.
    """
    
    def __init__(self, populacao, tamanho=10):
        super(Torneio, self).__init__(populacao)
        self.tamanho = tamanho
        
    def selecionar(self, fitness):
        """ Retorna o indivíduo campeão da rodada"""
        if fitness is None:
            fitness = self.populacao.avaliar()
        grupo = choice(fitness, size=self.tamanho)
        campeao = grupo.max()
        i = where(fitness == campeao)[0][0]
        return i
        