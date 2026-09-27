from numpy import exp, array
from pygenec.populacao import Populacao
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import mgrid 

def func(x, y):
    tmp = 3 * exp(-(y+1) **2 - x **2)*(x-1) **2 \
              - (exp(-(x+1) **2 -y **2)  / 3) \
              + exp(-x **2 - y **2) * (10 * x **3 - 2 * x + 10 * y ** 5)
              
    return tmp

def bin(x):
    cnt = array([2 ** i for i in range(x.shape[1])])
    return array([(cnt * x[i,:]).sum() for i in range(x.shape[0])])

def xy(populacao):
    colunas = populacao.shape[1]
    meio = colunas // 2
    maiorbin = 2.0 ** meio - 1.0
    nmin = -3
    nmax = 3
    const = (nmax - nmin) / maiorbin
    x = nmin + const * bin(populacao[:, :meio])
    y = nmin + const * bin(populacao[:, meio:])
    return x,y

def avaliacao(populacao):
    x, y = xy(populacao)
    tmp = func(x,y)
    return tmp

cromossos_totais = 8
tamanho_populacao = 5

populacao = Populacao(avaliacao, cromossos_totais, tamanho_populacao)
populacao.gerar_populacao()
populacao.avaliar()

x, y = xy(populacao.populacao)

fig = plt.figure(figsize=(100,100))
ax = fig.add_subplot(111, projection='3d')
X, Y = mgrid[-3:3:30j, -3:3:30j]
Z = func(X, Y)

ax.plot_wireframe(X, Y, Z)
ax.scatter(x, y, func(x, y), s=50, c='red', marker='D')
plt.show()
