

from firestore_model import Model
from google.cloud import firestore
from dataclasses import dataclass

from calle import Calle

@dataclass
class Nodo(Model):
    x:float
    y:float
    callesRefs: list
    def get_calles(self):
        for calle in self.callesRefs:
            yield Calle.get(calle)
            

    
