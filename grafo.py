import networkx as nx # importar el paquete de Networkx
import matplotlib.pyplot as plt #importar el paquete de graficas
G=nx.Graph()
#para poder agregar vertices o nodos

G.add_nodes_from(["A","B","C","D","E","F"])
#para poder agregar las aristas
G.add_edge("A","B")
G.add_edge("A","C")
G.add_edges_from([("C","D"),("D","E"),("F","C")])
#Cantidad nodos, cantidad de vertices, cuales son los nodos, cuales aristas
print(len(G.nodes)) #Cantidad de nodos
print(len(G.edges)) #Cantidad de aristas
print(G.nodes) #mostrar la etiqueta de todos los nodos
print(G.edges) #mostrar cuales vertices estan relacionados
nx.draw(G,with_labels=True,node_size=150)
plt.show()