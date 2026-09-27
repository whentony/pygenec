from numpy import array
from numpy.random import randint, random

class NoCompatibleIndividualSize(Exception):
    pass

class Cruzamento:
    """
    Class abstrata representando o cruzamento.
    
    Entrada:
    tamanho_populacao: tamanho da população para o cruzamento.
    """
    
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        
    def cruzamento(self, progenitor1, progenitor2):
        raise NotImplementedError("Método 'cruzamento' deve ser implementado pelas subclasses.")
    
    def descendentes(self, subpopulacao, pcruz):
        """
        Retorna uma nova população de tamanho_populacao
        através do cruzamento.
        
        Entrada:
            subpopulacao: lista de indivíduos da subpopulação.
            pcruz: probabilidade de cruzamento entre os indivíduos da subpopulação.
        """
        
        nova_populacao = []
        npop = len(subpopulacao)
        
        while(len(nova_populacao) < self.tamanho_populacao):
            i = randint(0, npop)
            j = randint(0, npop)
            while j == i and npop > 1:
                j = randint(0, npop)
                
            cruzar = random()
            if cruzar < pcruz:
                desc1, desc2 = self.cruzamento(subpopulacao[i], subpopulacao[j])
            else:
                desc1 = subpopulacao[i].copy()
                desc2 = subpopulacao[j].copy()

            nova_populacao.append(desc1)
            if len(nova_populacao) < self.tamanho_populacao:
                nova_populacao.append(desc2)

        return array(nova_populacao)