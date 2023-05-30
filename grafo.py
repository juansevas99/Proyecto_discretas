import itertools
import random
import networkx as nx # importar el paquete de Networkx
import matplotlib.pyplot as plt #importar el paquete de graficas
G=nx.Graph()




def held_karp(dists):

    n = len(dists)

    C = {}


    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2**n - 1) - 1

    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    path.append(0)

    return opt, list(reversed(path))


def generate_distances(n):
    dists = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dists[i][j] = dists[j][i] = random.randint(1, 99)

    return dists


def read_distances(filename):
    dists = []
    with open(filename, 'rb') as f:
        for line in f:
            # Skip comments
            if line[0] == '#':
                continue

            dists.append(map(int, map(str.strip, line.split(','))))

    return dists


if __name__ == '__main__':



    dists = [[0, 2.4, 5.8, 7.1, 10.8, 12.8, 12.1],
            [2.4, 0, 4.2 ,5.5 ,9.1 ,11.1, 10.5],
            [5.8, 4.2, 0 ,3.5, 7.4, 9.4 ,8.8],
            [7.1, 5.5 ,3.5, 0 ,4.4, 6.4, 5.8],
            [10.8 ,9.1, 7.4, 4.4, 0, 2.0 ,1.4],
            [12.8, 11.1 ,9.4 ,6.4, 2.0, 0, 3.0],
            [12.1, 10.5 ,8.8 ,5.8 ,1.4, 3.0, 0]]


 

 
    print(held_karp(dists))
    listaVertices=["Playa las torpedereas", "Museo Maritimo","Sebastiana" ,"Matematcias PUCV","Reloj de las flores" ,"Museo Wulff" ,"Quinta vergara"]
    G.add_nodes_from(listaVertices)
    cont=0
    cont1=0
    for line in dists:
        cont1=0
        for i in line:
            G.add_edge(listaVertices[cont],listaVertices[cont1]  , weight=i )
            cont1+=1
        cont+=1
    nx.draw(G)
    plt.show()

    cumple=1
    for i in range(7):
      for j in range(7):
        if (G.degree[listaVertices[i]]+ G.degree[listaVertices[i]]>=  7):
          cumple=0
    
    if (cumple==1):
      print("Este grafo es completo y por lo tanto hamiltoniano")
    else:
      print("Es un grafo incompleto y no hamiltoniano")


