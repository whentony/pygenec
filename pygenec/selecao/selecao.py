from numpy import array

class Selecao:
    """
    Seleciona indivíduos para cruzamento.
    Recebe como entrada:
    - populacao: array com os indivíduos da população.
    """
    
    def __init__(self, populacao):
        self.populacao = populacao
        
    def selecionar(self):
        """
        Retorna a lista de índice do vetor população
        dos indivíduos selecionados.
        """
        raise NotImplementedError("O método selecionar deve ser implementado pela subclasse.")
    
    def selecao(self, n, fitness=None):
        """
        Retorna uma população de tamanho n,
        selecionada via método selecionar.
        """
        
        progenitores = array([self.selecionar(fitness) for _ in range(n)])
        return self.populacao.populacao[progenitores]