import os
import time
from mapa import Mapa


class Menu():
    
    
    def __init__(self):
        self.fileMap = ""
        self.players = 0
        self.starts = []
        e = -1
        os.system("clear")
        print("+-------------------------------------------------------+")
        print("|                                                       |")
        print("|  / )( (  __/ __(_  _/  (  _ \  (  _ \/ _\ / __(  __)  |")
        print("|  \ \/ /) _( (__  )((  O )   /   )   /    ( (__ ) _)   |")
        print("|   \__/(____\___)(__)\__(__\_)  (__\_\_/\_/\___(____)  |")
        print("|                                                       |")
        print("+-------------------------------------------------------+")
        print("|     MAPAS:                                            |")
        print("+-------------------------------------------------------+")
        print("|        [1] - Mapa Praia                               |")
        print("|        [2] - Mapa Montanha                            |")
        print("|        [3] - Mapa Deserto                             |")
        print("|        [4] - Mapa Pista                               |")
        print("+-------------------------------------------------------+")
        
        while 1:
            e = int(input("Escolha o seu mapa: "))
    
            if (e == 1):
                m = Mapa("Praia")
                os.system('clear')
                break
            elif (e == 2):
                m = Mapa("Montanha")
                os.system('clear')
                break
            elif (e == 3):
                m = Mapa("Deserto")
                os.system('clear')
                break
            elif (e == 4):
                m = Mapa("Pista")
                os.system('clear')
                break
            else:
                print("Opção inválida...")
        self.fileMap = m
        
        os.system("clear")
        
        print("+-------------------------------------------------------+")
        print("|                                                       |")
        print("|  / )( (  __/ __(_  _/  (  _ \  (  _ \/ _\ / __(  __)  |")
        print("|  \ \/ /) _( (__  )((  O )   /   )   /    ( (__ ) _)   |")
        print("|   \__/(____\___)(__)\__(__\_)  (__\_\_/\_/\___(____)  |")
        print("|                                                       |")
        print("+-------------------------------------------------------+")
        print("|     JOGADORES:                                        |")
        print("+-------------------------------------------------------+")
        print("|        [1] - 1 Jogador                                |")
        print("|        [2] - 2 Jogadores                              |")
        print("+-------------------------------------------------------+")
        
        self.players = int(input("Escolha o número de jogadores: "))
        os.system("clear")


        
        
    def menu1(self):
        saida = -1
        while 1:
            print("****************************************\n*                 MENU                 *\n****************************************\n*                                      *")
            print("*   [1] - Imprimir Mapa                *")
            print("*   [2] - Imprimir Grafo               *")
            print("*   [3] - Imprimir Nodos do Grafo      *")
            print("*   [4] - Imprimir Arestas do Grafo    *")
            print("*   [5] - DFS                          *")
            print("*   [6] - BFS                          *")
            print("*   [7] - GREEDY                       *")
            print("*   [8] - ASTAR                        *")
            print("*   [0] - Sair                         *")
            print("*                                      *")
            print("****************************************")
            
            
            saida = int(input("Escolha uma opção: "))
            print('\n')
        return saida
        
    def menu2(self, map, final, graph):
        
        
        saida = -1
        while 1:
            print("****************************************\n*                 MENU                 *\n****************************************\n*                                      *")
            print("*   [1] - Imprimir Mapa                *")
            print("*   [2] - Imprimir Grafo               *")
            print("*   [3] - Imprimir Nodos do Grafo      *")
            print("*   [4] - Imprimir Arestas do Grafo    *")
            print("*   [5] - Modos de Travessia           *")
            print("*   [0] - Sair                         *")
            print("*                                      *")
            print("****************************************")
            
            
            saida = int(input("Escolha uma opção: "))
            print('\n')
            if saida == 0:
                print("Terminando Programa...")
                time.sleep(1)
                os.system('clear')
                break

            elif saida == 1:
                self.fileMap.printMap()
                input("Pressione qualquer tecla para avançar. ")
                os.system("clear")


            elif saida == 2:
                print(graph)
                input("Pressione qualquer tecla para avançar. ")
                os.system("clear")
                
                
            elif saida == 3:
                print(graph.m_nodes)
                input("Pressione qualquer tecla para avançar. ")
                os.system("clear")
                
                
            elif saida == 4:
                print(graph.imprime_aresta())
                input("Pressione qualquer tecla para avançar. ")
                os.system("clear")


            elif saida == 5:
                results = self.menuTravessia(map,graph,final)
                self.fileMap.showFinalmap(map,results)
                input("Pressione qualquer tecla para avançar. ")
                os.system("clear")


            else:
                print("Opção inválida!")
                time.sleep(0.7)
                os.system("clear")
                
                
            
            
    def posicaoInicial(self,map,i):
        x = len(map[0])-2
        y = len(map)-2
        x1 = -1
        y1 = -1
        while (x1 > x or x1 < 0 or y1 > y or y1 < 0):
            x1 = int(input("Escolha a coordenada inicial válida X do Jogador" + str(i) + " entre 1 e " + str(x) + ": "))
            y1 = int(input("Escolha a coordenada inicial válida Y do Jogador" + str(i) + " entre 1 e " + str(y) + ": "))
            if (x1 > x or x1 < 0 or y1 > y or y1 < 0 ):
                print("Coordenadas inválidas!")
            
            elif (map[y1][x1] == "X"):
                print("Coordenadas inválidas!")
                x1 = -1
                y1 = -1
                    

            
        print("\n****\nCoordenadas inciais do Jogador1: (" + str(x1) + ', ' + str(y1) + ")\n****")
        start = str((x1,y1,0,0))
        self.starts.append(start)
        return str((x1,y1,0,0))
            
            
    

                
    def menuTravessia(self,map,graph,final):
        results = []
        os.system("clear")
        print("****************************************\n*              TRAVESSIA               *\n****************************************\n*                                      *")
        print("*   [1] - DFS                          *")
        print("*   [2] - BFS                          *")
        print("*   [3] - GREEDY                       *")
        print("*   [4] - ASTAR                        *")
        print("*                                      *")
        print("****************************************")
        
        i = 0
        while (i<self.players):
            print('\n')
            self.fileMap.printMap()
            print('\n')
            saida = int(input("Escolha uma opção de de corrida para o Jogador" + str(i) + ": "))
            
            if (saida > 4 or saida < 1):
                print("Por favor selecione corretamente a travessia do grafo!")
                continue
            start = self.posicaoInicial(map,i)
            
            
            if saida == 1:
                result = graph.procura_DFS(start,final, path=[], visited=set())
                results.append(result[0])
                
                print("\n___________________________________________________________")
                print("Resultados da DFS: ")
                print(result[0])
                print("Com um custo total de : ["+ str(result[1]) + "]")
                print("___________________________________________________________")
                

            elif saida == 2:
                result = graph.procura_BFS(start,final)
                results.append(result[0])

                print("\n___________________________________________________________")
                print("Resultados da BFS: ")
                print(result[0])
                print("Com um custo total de : ["+ str(result[1]) + "]")
                print("___________________________________________________________")

                
            elif saida == 3:
                result = graph.greedy(start,final)
                results.append(result[0])

                print("\n___________________________________________________________")
                print("Resultados da GREEDY: ")
                print(result[0])
                print("Com um custo total de : ["+ str(result[1]) + "]")
                print("___________________________________________________________")


            elif saida == 4:
                result = graph.aStar(start,final)
                results.append(result[0])

                print("\n___________________________________________________________")
                print("Resultados da ASTAR: ")
                print(result[0])
                print("Com um custo total de : ["+ str(result[1]) + "]")
                print("___________________________________________________________")


            i += 1
        input("Pressione alguma tecla para avançar para a simulação da corrida: ")
        return results
            
            