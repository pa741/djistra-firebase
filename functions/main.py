import firestore_model
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from typing import Any

#from calle import Calle
#from nodo import Nodo
from firebase_functions import https_fn, options
import overpassGraph
# Use the application default credentials.
#c1 = Calle.make(nombre="garnacha", distancia=2, save=True)
#
#n1 = Nodo.make(x=1, y=2, name="n1", callesRefs=[c1.id])
#n1.save()
#c1.save()



@https_fn.on_call(region="europe-west1")
def addPedido(req: https_fn.CallableRequest) -> https_fn.Response:
    calleId = req.args.get("calle")
    print("Hello")
    return https_fn.Response(f"Message with ID  added.")


@https_fn.on_call(region="europe-west1")
def reset(req: https_fn.CallableRequest) -> https_fn.Response:
    
    print("Hello")
    return https_fn.Response(f"Message with ID  added.")