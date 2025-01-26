
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
@https_fn.on_request(region="europe-west1")
def addPedido(req: https_fn.Request) -> https_fn.Response:
    print(req)
    calleId = req
    print("Hello")
    add_pedido(calleId)
    return https_fn.Response(f"Message with ID  added.")


@https_fn.on_request(region="europe-west1")
def reset(req: https_fn.Request) -> https_fn.Response:
    
    print("Hello")
    return https_fn.Response(f"Message with ID  added.")