class Evoluacao:
    """
    Usando operadores genéticos, coloca uma população para evoluir.
    
    Entrada:
        populacao - a população inicial a ser evoluída.
        selecao - Objeto do tipo Selecao
        cruzamento - Objeto do tipo Cruzamento
        mutacao - Objeto do tipo Mutacao
    """
    
    def __init__(self, populacao, selecao, cruzamento, mutacao):
        self.populacao = populacao
        self.selecao = selecao
        self.cruzamento = cruzamento
        self.mutacao = mutacao
        
        self._geracao = 0
        self._melhor_solucao = None
        self._nsele = None
        self._ncruz = None
        
    def _set_nsele(self, nsele):
        self._nsele = nsele
        
    def _get_nsele(self):
        return self._nsele

    def _set_ncruz(self, ncruz):
        self._ncruz = ncruz
        
    def _get_ncruz(self):
        return self._ncruz
    
    @property
    def melhor_solucao(self):
        return self._melhor_solucao
    
    @property
    def geracao(self):
        return self._geracao
    
    def evoluir(self):
        """
        Executa uma iteração de evolução na população.
        """
        if self._first is True:
            self._fitness = self.populacao.avaliar()
            self._first = False
        
        self._melhor_solucao = self.populacao.populacao[-1].copy()
        
        subpopulacao = self.selecao.selecao(self._nsele, fitness=self._fitness)
        populacao = self.cruzamento.descendentes(subpopulacao, pcruz=self._ncruz)
        
        self.mutacao.populacao = populacao
        self.mutacao.mutacao()
        self.populacao.populacao[:] = populacao[:]
        
        self._geracao += 1
        
        if self._manter_melhor is True:
            self.populacao.populacao[0] = self._melhor_solucao
            
        self._fitness = self.populacao.avaliar()
        
        return self._fitness.min(), self._fitness.max()