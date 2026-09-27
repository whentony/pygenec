from numpy.random import randint, random
from numpy import array

from .cruzamento import NoCompatibleIndividualSize, Cruzamento

class KPontos(Cruzamento):
    """
    Gerador de população via cruzamento usando operador de k pontos.
    Entrada:
        tamanho_populacao - Tamanho da população a ser gerada via cruzamento.
    """
    
    def __init__(self, tamanho_populacao):
        super(KPontos, self).__init__(tamanho_populacao)
        
    def cruzamento(self, progenitor1, progenitor2):
        """
        Cruzamento via k-pontos de dois indivíduos.

        Args:
            progenitor1 (_type_): _description_
            progenitor2 (_type_): _description_
        """
        
        n1 = len(progenitor1)
        n2 = len(progenitor2)
        if n1 != n2:
            msg = "Tamanho ind1 {0} diferente do tamanho ind2 {1}".format(n1, n2)
            raise NoCompatibleIndividualSize(msg)
        
        
        desc1 = progenitor1.copy()
        desc2 = progenitor2.copy()
        kp = randint(1, max(2, n1 - 1))
        k = []
        while len(k) < kp:
            p = randint(1, n1)
            if p not in k:
                k.append(p)
        k.sort()

        pontos = [0] + k + [n1]
        troca = randint(0, 2)
        
        for i in range(len(pontos) - 1):
            if troca == 1:
                desc1[pontos[i]:pontos[i + 1]] = progenitor2[pontos[i]:pontos[i + 1]]
                desc2[pontos[i]:pontos[i + 1]] = progenitor1[pontos[i]:pontos[i + 1]]
            troca = 1 - troca
                
        return desc1, desc2
