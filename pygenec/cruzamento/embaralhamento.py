from numpy.random import shuffle, randint
from .cruzamento import NoCompatibleIndividualSize, Cruzamento

def cruzamento(selfself, progenitor1, progenitor2):
    """
    Cruzamento de dois individuos via embaralhemnto um ponto.
    
    O tamanho de ambos os indivíduos deve ser igual, do contrário um erro será levantado.

    Args:
        selfself (_type_): _description_
        progenitor1 (_type_): _description_
        progenitor2 (_type_): _description_
    """
    
    n1 = len(progenitor1)
    n2 = len(progenitor2)
    if n1 != n2:
        msg = "Tamanho ind1 {0} diferente do tamanho ind2 {1}".format(n1, n2)
        raise NoCompatibleIndividualSize(msg)

    order = list(range(n1))
    shuffle(order)
   
    ponto = randint(1, n1 - 1)

    desc1 = progenitor1.copy()
    desc2 = progenitor2.copy()
    
    desc1[:] = desc1[order]
    desc2[:] = desc2[order]
    
    desc1[:ponto], desc2[:ponto] = desc2[:ponto], desc1[:ponto]
    
    tmp1 = desc1.copy()
    tmp2 = desc2.copy()
    
    for i, j in enumerate(order):   
        desc1[j] = tmp1[i]
        desc2[j] = tmp2[i]

    return desc1, desc2