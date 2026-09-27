from numpy import array

class Selecao:
    """
    Seleciona indivíduos para cruzamento.
    Recebe como entrada:
    - populacao: array com os indivíduos da população.
    """
    
    def __init__(self, populacao):
        self.populacao = populacao
        
        