import overpass
from faker import Faker

from calle import Calle
from nodo import Nodo
from firebase_admin import firestore
import firebase_admin


def CreateGraph():


    fake = Faker("es_ES")
    api = overpass.API()
    response = api.get('area[name = "Fuenmayor"];(way(area)["highway"];>;);')
    nodesPosDict = {}

    nodesStreetDict = {} # nodeId -> set of waysIds
    streetNodesDict = {} # wayId -> set of node ids
    firebase_admin.initialize_app()
    wayDict = {}
    nodeDict = {}
    db = firestore.client()

    docsCalles = db.collection("Calle").list_documents()
    docsNodos = db.collection("Nodo").list_documents()

    for doc in docsCalles:
        doc.delete()
    for doc in docsNodos:
        doc.delete()

    typesSet = set()

    for way in response['features']:
        props = way['properties']
        nodes = props['nodes']
        id = props['id']
        geo = way['geometry']
        coords = geo['coordinates']
        tags = props['tags']
        highway = tags['highway']
        name = tags.get('name', fake.unique.street_name())

        if highway != "residential" and highway != "tertiary" and highway != "secondary":
            continue

        typesSet.add(highway)
        street = streetNodesDict.setdefault(id,set())
        street.update(nodes)
        
        geoStr = ""
        if geo.get('type') == "LineString":
            geoStr = str(geo['coordinates'])
            
        
        c = Calle.make(nombre=name, nodosRefs=nodes, geo=geoStr)
        c.id = str(id)
        wayDict[id] = c
        if(not coords):
            continue
        for i in range(len(nodes)):
            ways = nodesStreetDict.setdefault(nodes[i], set())
            if id not in ways:
                ways.add(id)
                
            n = nodes[i]
            try:
                nodePos = coords[i]
            except:
                print("Error")
                print(way)
                print(nodes)
                print(coords)
                continue
            nodesPosDict[n] = nodePos
            
    for node in nodesPosDict:
        n = nodesPosDict[node]
        x = n[0]
        y = n[1]
        calles = nodesStreetDict[node]
        nodo = Nodo.make(x=x, y=y, callesRefs=calles)
        nodo.id =  str(node)
        nodeDict[node] = nodo
        

    for way in wayDict:
        wayDict[way].save()
    for node in nodeDict:
        nodeDict[node].save()




#print(nodesPosDict)

## Dict de nodos con una lista de calles a las que apuntan
## luego me recorro los nodos inicializando Nodo.py haciendo que apunte a sus calles, creando Calle.py si no existe
## Obtengo las calles de un dictionario de calles,  de forma que si ya existe la calle, no la vuelvo a crear
## Guardo todos los nodos y las calles en firebase.