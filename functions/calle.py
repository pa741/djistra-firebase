
import firebase_admin.firestore
from firestore_model import Model
import firebase_admin 
from dataclasses import dataclass


@dataclass
class Calle(Model):
  nombre:str
  esRuta: bool
  esPedido: bool
  nodosRefs: list
  geo: str
  def get_all():
    calles = []
    db = firebase_admin.firestore.client()
    docs = db.collection("Calle").list_documents()
    for doc in docs:
      calle = Calle.get(doc.id)
      calles.append(calle)
    return calles
  

  
