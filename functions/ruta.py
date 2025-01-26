
from firestore_model import Model
from google.cloud import firestore
from dataclasses import dataclass

@dataclass
class Ruta(Model):
  callesref: list
  nodosref: list
  
