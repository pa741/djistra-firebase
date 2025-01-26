
from firestore_model import Model
from google.cloud import firestore
from dataclasses import dataclass

@dataclass
class Calle(Model):
  nombre:str
 
  nodosRefs: list
  geo: str

  
