from numpy.random import randint
from numpy import array

from .cruzamento import NotCompatibleIndividualSize, Cruzamento

class UmPonto(Cruzamento):
    """
    Gerador de população via cruzamento usando operador de um ponto.
    Entrada:
        tamanho_populacao - Tamanho da população a ser gerada via cruzamento.
    """
    
    def __init__(self, tamanho_populacao):
        super(UmPonto, self).__init__(tamanho_populacao)

    def cruzamento(self, progenitor1, progenitor2):
        """ 
           Cruzamento de dois indivíduos via um ponto.
           Entrada:
               ind1 - Primeiro indivíduo
               ind2 - Segundo indivíduo
               
           O tamanho de ambos os indivíduos deve ser igual, do contrário um erro será levantado.
           """
           
        n1 = len(progenitor1)
        n2 = len(progenitor2)
        if n1 != n2:
            msg = "Tamanho ind1 {0} diferente do tamanho ind2 {1}".format(n1, n2)
            raise NotCompatibleIndividualSize(msg)

        ponto = randint(1, n1 -1)
        desc1 = progenitor1.copy()
        desc2 = progenitor2.copy()

        desc1[ponto:] = progenitor2[ponto:]
        desc2[ponto:] = progenitor1[ponto:]

        return desc1, desc2