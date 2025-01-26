
from calle import Calle
from ruta import Ruta
from nodo import Nodo


        
class Djikstra:
    def __init__(self, nodos: dict, calles: dict,startCalle: str):
        self.nodos = nodos
        self.calles = calles
        self.camino = {}
        self.cola = []
        self.visited = []
        self.distances = {}
        self.previous = {}
        self.startCalle = startCalle
    
    
    def get_distance(self, node1: Nodo, node2: Nodo):
        return ((node1.x - node2.x)**2 + (node1.y - node2.y)**2)**0.5
    
    def calculate_distances(self):
        for node in self.nodos:
            self.distances[node.id] = float("inf")
            self.previous[node.id] = None
        for nodos in self.calles[self.startCalle].nodosRefs:
            self.distances[nodos] = 0
            self.cola.append(self.nodos[nodos])
            self.visited.append(self.nodos[nodos])
        while self.cola:
            self.cola.sort(key=lambda x: self.distances[x.id])
            current = self.cola.pop(0)
            for calle in current.callesRefs:
                calle = self.calles[calle]
                for nodo in calle.nodosRefs:
                    nodo = self.nodos[nodo]
                    if nodo in self.visited:
                        self.cola.append(nodo)
                        self.visited.append(nodo)
                    if self.distances[current.id] + self.get_distance(current, nodo) < self.distances[nodo.id]:
                        self.distances[nodo.id] = self.distances[current.id] + self.get_distance(current, nodo)
                        self.previous[nodo.id] = current.id
                        self.nodos[nodo.id].distancia = self.distances[nodo.id]
                        self.nodos[nodo.id].save()
        
          
        
        



def add_pedido(calle_id: str) -> str:
    nodos = Nodo.get_all()
    nodosDict = {}
    calles = Calle.get_all()
    callesDict = {}
    for nodo in nodos:
        nodosDict[nodo.id] = nodo
        nodo.distancia = 1000
        nodo.save()
    for calle in calles:
        callesDict[calle.id] = calle
    djikstra = Djikstra(nodosDict, callesDict, calle_id)
    djikstra.calculate_distances()
    AddPedidoToRuta(djikstra)
    
    
def AddPedidoToRuta( djikstra: Djikstra):
    ruta  = Ruta.get("ruta"); 
    calles = djikstra.calles
    calles_ruta = ruta.callesref
    min_distance = float("inf")
    for calle in calles_ruta:
        c = calles[calle]
        for nodo in c.nodosRefs:
            if djikstra.distances[nodo] < min_distance:
                min_distance = djikstra.distances[nodo]
                min_nodo = nodo
    if min_nodo:
        min_dist = float("inf")
        indexofMin = ruta.nodosref.index(min_nodo)
        min_next = None
        #check next and previous nodes to see if they are closer
        if indexofMin + 1 < len(ruta.nodosref):
            next_nodo = ruta.nodosref[indexofMin + 1]
            if djikstra.distances[next_nodo] < min_dist:
                min_dist = djikstra.distances[next_nodo]
                min_next = next_nodo
        if indexofMin - 1 >= 0:
            previous_nodo = ruta.nodosref[indexofMin - 1]
            if djikstra.distances[previous_nodo] < min_dist:
                min_dist = djikstra.distances[previous_nodo]
                min_next = previous_nodo
        if min_next:
            indexofMinNext = ruta.nodosref.index(min_next)
            for i in range(indexofMin + 1, indexofMinNext):
                ruta.nodosref.pop(i)         
            
            addNodosToRuta(djikstra.previous, min_next, ruta)
        addNodosToRuta(djikstra.previous, min_nodo, ruta)
        


def addNodosToRuta(previous:dict, nodo_id: str, ruta: Ruta):
    if previous[nodo_id]:
        addNodosToRuta(previous, previous[nodo_id], ruta)
    ruta.nodosref.append(nodo_id)
    ruta.save()

        
    

        
    
    
    