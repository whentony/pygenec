from numpy import exp, array
from pygenec.evolucao import Evoluacao
from pygenec.mutacao.flip import Flip
from pygenec.populacao import Populacao
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from numpy import mgrid 
from pygenec.selecao.roleta import Roleta
from pygenec.selecao.classificacao import Classificacao
from pygenec.selecao.torneio import Torneio
from numpy import unique
from pygenec.populacao import Populacao
from pygenec.cruzamento.kpontos import KPontos

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

cromossos_totais = 32
tamanho_populacao = 50

populacao = Populacao(avaliacao, cromossos_totais, tamanho_populacao)
populacao.gerar_populacao()

selecao = Roleta(populacao)
cruzamento = KPontos(tamanho_populacao)
mutacao = Flip(pmut=0.9)
evolucao = Evoluacao(populacao, selecao, cruzamento, mutacao)

evolucao.nsele = 10
evolucao.ncruz = 0.5

fig = plt.figure(figsize=(100,100))
ax = fig.add_subplot(111, projection='3d')
X, Y = mgrid[-3:3:30j, -3:3:30j]
Z = func(X, Y)

ax.plot_wireframe(X, Y, Z)
x, y = xy(populacao.populacao)
graph = ax.scatter(x, y, func(x, y), s=50, c='red', marker='D')

print("=" * 75)
print("  GERAÇÃO   |   MELHOR X   |   MELHOR Y   |   MELHOR FITNESS (Z)  |  STATUS")
print("=" * 75)

def update(frame):
    fmin, fmax = evolucao.evoluir()
    x, y = xy(populacao.populacao)
    graph._offsets3d = (x, y, func(x, y))
    
    melhor_z = fmax
    melhor_x = x[-1]
    melhor_y = y[-1]
    
    ax.set_title(f"Evolução em Tempo Real | Geração: {evolucao.geracao} | Melhor Z: {melhor_z:.4f}")
    
    # Imprime no terminal a cada 5 gerações ou na primeira
    if evolucao.geracao % 5 == 0 or evolucao.geracao == 1:
        status = "🚀 Subindo" if melhor_z < 7.5 else "🏆 No Topo!"
        print(f"  Gen {evolucao.geracao:4d}  |   {melhor_x:8.4f}   |   {melhor_y:8.4f}   |        {melhor_z:8.4f}       | {status}")

ani = FuncAnimation(fig, update, frames=50, interval=50, repeat=False)    

print("=" * 75)

# 1. Demonstração de Cruzamento com os melhores indivíduos
p1 = populacao.populacao[0]
p2 = populacao.populacao[-1]
f1, f2 = cruzamento.cruzamento(p1, p2)

p1_x, p1_y = xy(array([p1]))
p2_x, p2_y = xy(array([p2]))
f1_x, f1_y = xy(array([f1]))
f2_x, f2_y = xy(array([f2]))

str_p1 = ''.join(str(b) for b in p1)
str_p2 = ''.join(str(b) for b in p2)
str_f1 = ''.join(str(b) for b in f1)
str_f2 = ''.join(str(b) for b in f2)

print("\n" + "=" * 82)
print("                      🧬 TABELA DE CRUZAMENTO (CROSSOVER)")
print("=" * 82)
print(f" {'Indivíduo':<10} | {'Genes (Cromossomo)':<34} | {'X':<7} | {'Y':<7} | {'Fitness (Z)':<11}")
print("-" * 82)
print(f" {'Pai 1':<10} | {str_p1:<34} | {p1_x[0]:<7.3f} | {p1_y[0]:<7.3f} | {func(p1_x, p1_y)[0]:<11.4f}")
print(f" {'Pai 2':<10} | {str_p2:<34} | {p2_x[0]:<7.3f} | {p2_y[0]:<7.3f} | {func(p2_x, p2_y)[0]:<11.4f}")
print("-" * 82)
print(f" {'Filho 1':<10} | {str_f1:<34} | {f1_x[0]:<7.3f} | {f1_y[0]:<7.3f} | {func(f1_x, f1_y)[0]:<11.4f}")
print(f" {'Filho 2':<10} | {str_f2:<34} | {f2_x[0]:<7.3f} | {f2_y[0]:<7.3f} | {func(f2_x, f2_y)[0]:<11.4f}")
print("=" * 82)

# 2. Imprime os detalhes da melhor solução encontrada
melhor_individuo = populacao.populacao[-1:]
melhor_x, melhor_y = xy(melhor_individuo)
melhor_z = func(melhor_x, melhor_y)

print("\n" + "=" * 50)
print("           🏆 MELHOR SOLUÇÃO ENCONTRADA")
print("=" * 50)
print(f"Gerações executadas : {evolucao.geracao}")
print(f"Coordenada X        : {melhor_x[0]:.6f}")
print(f"Coordenada Y        : {melhor_y[0]:.6f}")
print(f"Valor Máximo (Z)    : {melhor_z[0]:.6f}")
print(f"Cromossomo Binário  : {''.join(str(b) for b in melhor_individuo[0])}")
print("=" * 50 + "\n")
plt.show()







