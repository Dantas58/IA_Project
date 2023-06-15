import math
from nodo import Node
from grafo import Graph
from queue import Queue

class Procura():
    
    
    def __init__(self,start, final, map):
        self.grafo = Graph(directed=True)
        self.start = start
        self.final = final
        self.map = map
    
    def cria_grafo(self):
        
        
        paraExpandir = []
        paraExpandir.append(self.start)
        
        
        expandidos = set()
        
        while len(paraExpandir) > 0: # vai à Queue e aplica a "expande" a cada estado
            estado = paraExpandir.pop(0)
            expandir  = self.expande(estado)
            expandidos.add(estado)
            estima = self.calculaDistancia(estado,self.final)
            self.grafo.add_heuristica((estado),estima)
            
            if len(expandir) == 0:
                continue
            
            for est, peso in expandir:
                self.grafo.add_edge(estado,est,peso)
                
                if est not in expandidos and est not in paraExpandir:
                    paraExpandir.append(est)
                    expandidos.add(est)
        
        
        
        
        
    def calculaDistancia(self,estado, est):
        x1 = estado[0]
        y1 = estado[1]
        x2 = est[0]
        y2 = est[1]
        a = (x2-x1)**2 + (y2-y1)**2
        b = math.sqrt(a)
        return int(b)



    def expande(self,estado):
        
        posX = estado[0]
        posY = estado[1]
        velX = estado[2]
        velY = estado[3]

        1
        if (self.map[posY][posX] == "X"): # quando sai do mapa ou bate na parede
            posX = posX-velX
            posY = posY-velY
            return [((posX,posY,0,0),25)]
        
        acel = [(0,1), (0,-1), (1,0), (1,1), (1,-1), (-1,1), (-1,0), (0,0),(-1,-1)]      # todas as acelerações possíveis
        
        
        if (velX == 0 and velY == 0):   # quando a velocidade é (0,0) nao pode ter a aceleração (0,0) senão ia estar parado
            acel.remove((0,0))
            
        
        jogadas = []        
        
        for a in acel:
            x = self.aplicaAceleracao(estado,a)
            if(x is not None):
                x1 = x[0][0]
                y1 = x[0][1]
                if (x1 < 0 or x1 >= len(self.map[0]) or y1 < 0 or y1 >= len(self.map)):
                    continue
                jogadas.append(x)
        
        return jogadas
            
    
    
    def aplicaAceleracao(self,estado, acel):
                
        posX = estado[0]
        posY = estado[1]
        velX = estado[2]
        velY = estado[3]
        
        
        velX = velX + acel[0]
        velY = velY + acel[1]
        posX1 = posX + velX
        posY1 = posY + velY
        
        if (posX1 < 0 or posX1 >= len(self.map[0]) or posY1 < 0 or posY1 >= len(self.map) or self.map[posY1][posX1] == "X"):
            return ((posX1,posY1,velX,velY),1)
        
        

        
        xP, xG = posX, posX1
        if velX < 0 :
            xP, xG = posX1, posX
        yP, yG = posY, posY1
        if velY < 0 :
            yP, yG = posY1, posY
              
    
        
        caminho = self.verifica(xP,xG,yP,yG)
        
        

        if caminho:  
            return ((posX1,posY1,velX,velY),1)
        return None
        
        
        
    def verifica(self, xP,xG, yP, yG):
        x1G = xG+1
        x1P = xP
        y1G = yG+1
        y1P = yP
        while x1G != x1P:
            if self.map[yP][x1P] == "X" or self.map[yG][x1P] == "X":
                return False
            x1P +=1
        
        while y1P != y1G:
            if self.map[y1P][xP] == "X" or self.map[y1P][xG] == "X":
                return False
            y1P +=1
                
        return True
        