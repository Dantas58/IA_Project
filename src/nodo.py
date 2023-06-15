class Node:



    def __init__(self,tuple):   # tuplo do tipo (x, y, vX, vY)
        self.tuple = tuple
        
        
    def __str__(self):
        return (str(self.tuple))
    
    #Devolve representação 'oficial' do objeto, neste caso particular pode ser igual a __str__
    def __repr__(self):
        return (str(self.tuple))

    
    def __eq__(self, other): # tipo "(x, y, vx, vy)"
        return (self.tuple == other.tuple)

    #Devolve o hash de um nodo. Ao implementar o método __eq__
    #torna-se também necessário definir __hash__. Caso
    #contrário o objeto torna-se unhashable
    def __hash__(self):
        return hash(self.tuple)