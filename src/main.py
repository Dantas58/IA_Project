from Procura import Procura
from Menu import Menu


def main():
    
    menu = Menu()
    
    m = menu.fileMap 
    map = m.matrixMap()
    start = m.getStart(map)
    final = m.getFinal(map)
    
    
    solve = Procura(start,final,map)
    solve.cria_grafo()
    graph = solve.grafo
    
    menu.menu2(map,str(final),graph)
    
    
if __name__ == "__main__":
    main()
    
    
    
  