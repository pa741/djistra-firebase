
import os
import firestore_model
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import google.cloud.firestore
from typing import Any
app = firebase_admin.initialize_app()
firestore_client: google.cloud.firestore.Client = firestore.client()
firestore_model.db = firestore_client
#from calle import Calle
#from nodo import Nodo
from firebase_functions import https_fn, options
from pathfinding import add_pedido
import overpassGraph
# Use the application default credentials.
#c1 = Calle.make(nombre="garnacha", distancia=2, save=True)
#
#n1 = Nodo.make(x=1, y=2, name="n1", callesRefs=[c1.id])
#n1.save()
#c1.save()

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\pablo\\AppData\\Roaming\\gcloud\\application_default_credentials.json"

clientes = {"10154343916","10154351720","1155537579","1155537602","1425054312","2058832230"}

@https_fn.on_request(region="europe-west1")
def addPedido(req: https_fn.Request) -> https_fn.Response:
    calleId = req
    if calleId not in clientes:
        return https_fn.Response(f"Cliente no encontrado",status= 401)
    add_pedido(calleId)
    return https_fn.Response(f"Pedido agregado a la ruta.")


@https_fn.on_request(region="europe-west1")
def reset(req: https_fn.Request) -> https_fn.Response:
    
    print("Hello")
    return https_fn.Response(f"Message with ID  added.")