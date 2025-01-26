

from firestore_model import Model
import firestore_model
from dataclasses import dataclass
from firebase_admin import firestore

from calle import Calle



firestore_model.db = firestore.client()
@dataclass
class Nodo(Model):
    x:float
    y:float
    callesRefs: list
    distancia: float
    def get_calles(self):
        for calle in self.callesRefs:
            yield Calle.get(calle)
    def reset(self):
        self.save()
    def get_all():
        nodos = []
        db = firestore.Client()
        docs = db.collection("Nodo").list_documents()
        for doc in docs:
            nodo = Nodo.get(doc.id)
            nodos.append(nodo)
        return nodos
    
