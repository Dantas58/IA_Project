import time
from colorama import Fore, Back, Style
import os



class Mapa:
    def __init__(self,name):
        self.m_name = str(name)
    
    def __str__(self):
        return "Mapa: " + self.m_name
    
    def __rep__(self):
        return "Mapa: " + self.m_name
    
    def getName(self):
        return self.m_name
    
    def setName(self, name):
        self.m_name = name
        
    def __eq__(self, other):
        return self.m_name == other.m_name
    
    def __hash__(self):
        return hash(self.m_name)
    
    
    
    def printMap(self):
        
        with open("../maps/" + self.m_name+".txt","r") as f:
                print(f.read())
    
    
    def matrixMap(self):
        
        with open("../maps/" + self.m_name+".txt", 'r') as f: 
            matrix = [[peca for peca in line[:-1].split(' ')] for line in f]
        
        
        


        return matrix
    
    def getStart(self,matrix):
        start = ([(row.index('P'),index) for index, row in enumerate(matrix) if 'P' in row])
        x, y = tuple(start[0])
        return (x,y,0,0)
        
    def getFinal(self,matrix):
        final = ([(row.index('F'),index) for index, row in enumerate(matrix) if 'F' in row])
        x, y = tuple(final[0])
        return (x,y)

    
    
    def showFinalmap(self,matrix,positionsList):
        os.system('clear')
        

        if len(positionsList) == 1:
        
            for p in positionsList[0]:
                parse = p[1:].split(',')
                x = int(parse[0])
                y = int(parse[1])
                print("Localização Jogador0 (A): ("+ str(y) + ", " + str(x) + ")" )
                l = matrix[y][x]
                matrix[y][x] = "#"

                for linha in matrix:
                    for peca in linha:
                        if peca == "#":
                            print(Fore.GREEN + 'A ' + Style.RESET_ALL, end='')
                        else:
                            print(peca + ' ',end='')
                    print()
                matrix[y][x] = l    
                time.sleep(0.5)
                os.system('clear')
        
        else:
            if len(positionsList)> 1:
                
                len1 = len(positionsList[0])
                len2 = len(positionsList[1])
                
                if len1 > len2:
                    dif = len1-len2
                    r = positionsList[1][len2-1]
                    print("R" + r)
                    while (dif>0):
                        positionsList[1].append(r)
                        dif -=1
                        
                if len2 > len1:
                    dif = len2-len1
                    r = positionsList[0][len1-1]
                    while(dif>0):
                        positionsList[0].append(r)
                        dif -=1
                
                        

                
                positionsListZIP = zip(positionsList[0],positionsList[1])
                
                for(p1,p2) in positionsListZIP:
                    parse = p1[1:].split(',')
                    x1 = int(parse[0])
                    y1 = int(parse[1])
                    parse = p2[1:].split(',')
                    x2 = int(parse[0])
                    y2 = int(parse[1])
                    if (x1 == x2 and y1 == y2):
                        if matrix[y1][x1-1] != "X":
                            x1 = x1-1
                        elif matrix[y1-1][x1] != "X":
                            y1 = y1-1
                        elif matrix[y1-1][x1-1] != "X":
                            x1 = x1-1 
                            y1 = y1-1
                        
                    print("Localização Jogador0 (A): (" + str(x1) + ", " + str(y1) + ")  |  Localização Jogador1 (B): (" + str(x2) + ", " + str(y2) + ")")
                    l1 = matrix[y1][x1]
                    l2 = matrix[y2][x2]
                    
                    matrix[y1][x1] = "A"
                    matrix[y2][x2] = "B"
                    for linha in matrix:
                        for peca in linha:
                            if peca == "B":
                                print(Fore.RED + 'B ' + Style.RESET_ALL, end='')
                            elif peca == "A":
                                print(Fore.GREEN + 'A '+ Style.RESET_ALL, end='')
                            else:
                                print(peca + ' ',end='')
                        print()
                    matrix[y1][x1] = l1
                    matrix[y2][x2] = l2
                    time.sleep(0.5)
                    os.system("clear")                    
                   
                    
            
        
    