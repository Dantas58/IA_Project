import matplotlib.pyplot as plt
from queue import Queue

import math
from nodo import Node


class Graph:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed 
        self.m_graph = {}   
        self.m_h={}       



    ##############################
    # Escrever o grafo como string
    ##############################
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "Node " + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
    
    #####################################
    # Adicionar aresta no grafo, com peso
    ####################################
    def add_edge(self, node1, node2, weight):   #node1 e node2 são os 'nomes' de cada nodo
        n1 = Node((node1))     # cria um objeto node  com o nome passado como parametro
        n2 = Node((node2))     # cria um objeto node  com o nome passado como parametro
        if (n1 not in self.m_nodes):
            self.m_nodes.append(n1)
            self.m_graph[str(n1)] = list()
        else:
            n1 = self.get_node_by_name(node1)

        if (n2 not in self.m_nodes):
            self.m_nodes.append(n2)
            self.m_graph[str(n2)] = list()
        else:
            n2 = self.get_node_by_name(node2)

        self.m_graph[str(n1)].append((str(n2), weight))





    ################################
    # Encontrar nodo pelo nome
    ################################
    def get_node_by_name(self, node):
        search_node = Node(node)
        for n in self.m_nodes:
            if n == search_node:
                return n
        return None

    ###########################
    # Imprimir arestas
    ###########################
    def imprime_aresta(self):
        listaA = ""
        for nodo in self.m_graph.keys():
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    ################################
    # Devolver o custo de uma aresta
    ################################
    def get_arc_cost(self, node1, node2):
        custoT=math.inf
        a=self.m_graph[node1]    # lista de arestas para aquele nodo
        for (nodo,custo) in a:
            if nodo==node2:
                custoT=custo

        return custoT
    
    
    
    
    ###############################
    # Adiciona a heurística ao nodo
    ###############################
    def add_heuristica(self, n, estima):
            n1 = Node(n)
            if n1 in self.m_nodes:
                self.m_h[str(n)] = estima



    ######################################
    # Dado um caminho calcula o seu custo
    #####################################
    def calcula_custo(self, caminho):
        #caminho é uma lista de nomes de nodos
        teste=caminho
        custo=0
        i=0
        while i+1 < len(teste):
             custo=custo + self.get_arc_cost(teste[i], teste[i+1])
             i=i+1
        return custo


    ################################################################################
    # Procura DFS
    ####################################################################################
    def procura_DFS(self,start, end, path=[], visited=set()):
        path.append(start)
        visited.add(start)
        
        posStart = start[1:-1].split(",")
        x1 = posStart[0]
        y1 = posStart[1]
        posStart = "(" + str(x1) + "," + str(y1) + ")"
        
        
        
        if posStart == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT= self.calcula_custo(path)
            return (path, custoT)
        
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho......
        return None
    
    
    
    
    ################################################################################
    # Procura BFS
    ####################################################################################
     
    
    def procura_BFS(self, start, end):
        queue = Queue()             
        pais = {}
        visitados = []
        caminho = []
        
        queue.put(start)        
        pais[start] = set()     
        pais[start].add(start)  
                
        while not queue.empty(): 
            node = queue.get()
            visitados.append(node)  


        
            for(adj, valor) in self.m_graph[node]:      

                
                adjS = adj[1:-1].split(",")
                x1 = adjS[0]
                y1 = adjS[1]
                adjS = "(" + str(x1) + "," + str(y1) + ")"

                
                
                if adjS == end:              
                    pais[adj] = set()       
                    pais[adj].add(node)     
                    pai = adj
                    
                    while pai != start:
                        caminho.append(pai)
                        x = pais.get(pai)
                        pai = x.pop()
                    
                    caminho.append(pai)
                    caminho.reverse()
                    custoT= self.calcula_custo(caminho)
                    return (caminho, custoT)

                if adj not in visitados:        
                    queue.put(adj)          
                    pais[adj] = set()       
                    pais[adj].add(node)
        return None
        
    '''
        
    def procura_BFS(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()

        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:


            nodo_atual = fila.get()
            adjS = nodo_atual[1:-1].split(",")
            x1 = adjS[0]
            y1 = adjS[1]
            adj = "(" + str(x1) + "," + str(y1) + ")"
            if adj == end:
                path_found = True
                end = nodo_atual
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)



        # Reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)
    '''

    ###################################################
    # Devolve vizinhos de um nó
    ###################################################

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    
    ################################################################################
    # Procura GREEDY
    ####################################################################################


    def greedy(self, start, end):
        # open_list é uma lista de nodos visitados, mas com vizinhos
        # que ainda não foram todos visitados, começa com o  start
        # closed_list é uma lista de nodos visitados
        # e todos os seus vizinhos também já o foram
        open_list = set([start])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # encontraf nodo com a menor heuristica
            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None


            adjS = n[1:-1].split(",")
            x1 = adjS[0]
            y1 = adjS[1]
            adjS = "(" + str(x1) + "," + str(y1) + ")"

            
            
            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            if adjS == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))

            # para todos os vizinhos  do nodo corrente
            for (m, weight) in self.getNeighbours(n):
                # Se o nodo corrente nao esta na open nem na closed list
                # adiciona-lo à open_list e marcar o antecessor
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n


            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None



    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])

    
    
    ##########################################
    #    A*
    ##########################################

    def aStar(self, start, end):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}  ##  g é apra substiruir pelo peso  ???

        g[start] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start] = start
        n = None
        while len(open_list) > 0:
            # find a node with the lowest value of f() - evaluation function
            calc_heurist = {}
            flag = 0
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.getH(v)
            if flag == 1:
                min_estima = self.calcula_est(calc_heurist)
                n = min_estima
            if n == None:
                print('Path does not exist!')
                return None
            
            
            
            adjS = n[1:-1].split(",")
            x1 = adjS[0]
            y1 = adjS[1]
            adjS = "(" + str(x1) + "," + str(y1) + ")"
            
            
            

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if adjS == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                #print('Path found: {}'.format(reconst_path))
                return (reconst_path, self.calcula_custo(reconst_path))

            # for all neighbors of the current node do
            for (m, weight) in self.getNeighbours(n):  # definir função getneighbours  tem de ter um par nodo peso
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None



    ##########################################3
    #
    def calcula_est(self, estima):
        l = list(estima.keys())
        min_estima = estima[l[0]]
        node = l[0]
        for k, v in estima.items():
            if v < min_estima:
                min_estima = v
                node = k
        return node