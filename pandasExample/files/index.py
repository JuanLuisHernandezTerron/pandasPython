from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
client = MongoClient(os.getenv("URL_BBDD"))
db = client['F1']
escuderias = db.create_collection('escuderias')
escuderias.insert_one({"nombre":"AstonMartin","Campeonatos":"1"})