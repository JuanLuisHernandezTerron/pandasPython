# $eq: Coincide con documentos donde el valor del campo es igual al valor especificado.
# $ne: Coincide con documentos donde el valor del campo no es igual al valor especificado.
# $gt: Coincide con documentos donde el valor del campo es mayor que el valor especificado.
# $gte: Coincide con documentos donde el valor del campo es mayor o igual que el valor especificado.
# $lt: Coincide con documentos donde el valor del campo es menor que el valor especificado.
# $lte: Coincide con documentos donde el valor del campo es menor o igual que el valor especificado.
# $in: Coincide con documentos donde el valor del campo está en el conjunto especificado de valores.
# $nin: Coincide con documentos donde el valor del campo no está en el conjunto especificado de valores.
# $exists: Coincide con documentos que tienen el campo especificado.
# $type: Coincide con documentos donde el tipo de datos del campo coincide con el valor especificado.
# $regex: Coincide con documentos donde el valor del campo coincide con la expresión regular especificada.
# $or: Coincide con documentos que cumplen con al menos una de las condiciones especificadas.
# $and: Coincide con documentos que cumplen con todas las condiciones especificadas.
# $not: Invierte el efecto de una expresión de consulta que lo precede.
# $nor: Coincide con documentos que no cumplen con ninguna de las condiciones especificadas.

from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
client = MongoClient(os.getenv("URL_BBDD"))
db = client['F1']
# pilotos = db.create_collection('pilotos')
# escuderias = db.create_collection('escuderias')
# db.drop_collection('escuderias')
# escuderias.insert_one({"nombre":"AstonMartin","Campeonatos":1,"pilotos":[14,17]})
# escuderias.insert_one({"nombre":"Ferrari","Campeonatos":15,"pilotos":[55,16]})
# escuderias.insert_one({"nombre":"RedBull","Campeonatos":4,"pilotos":[33,3]})
# escuderias.insert_one({"nombre":"Mclaren","Campeonatos":12,"pilotos":[4,13]})
# escuderias.insert_one({"nombre":"Mercedes AMG F1","Campeonatos":8,"pilotos":[44,31]})
# escuderias.insert_one({"nombre":"Alpine","Campeonatos":2,"pilotos":[32,15]})

# pilotos.insert_one({"_id":14,"nombre":"Fernando Alonso","Campeonatos":2,"pais":"España"})
# pilotos.insert_one({"_id":55,"nombre":"Carlos Sainz","Campeonatos":0,"pais":"España"})
# pilotos.insert_one({"_id":33,"nombre":"Max Verstappen","Campeonatos":3,"pais":"Holanda"})
# pilotos.insert_one({"_id":4,"nombre":"Lando Norris","Campeonatos":0,"pais":"Inglaterra"})
# pilotos.insert_one({"_id":44,"nombre":"Lewis Hamilton","Campeonatos":5,"pais":"Inglaterra"})
# pilotos.insert_one({"_id":32,"nombre":"Esteban Ocon","Campeonatos":0,"pais":"Francia"})
# pilotos.insert_one({"_id":15,"nombre":"Pierre Gasly","Campeonatos":0,"pais":"Francia"})
# pilotos.insert_one({"_id":31,"nombre":"George Russell","Campeonatos":0,"pais":"Inglaterra"})
# pilotos.insert_one({"_id":13,"nombre":"Oscar Piastri","Campeonatos":0,"pais":"Australia"})
# pilotos.insert_one({"_id":3,"nombre":"Sergio Perez","Campeonatos":0,"pais":"Mexico"})
# pilotos.insert_one({"_id":17,"nombre":"Lance Stroll","Campeonatos":0,"pais":"Cánada"})
# pilotos.insert_one({"_id":16,"nombre":"Charles Leclrecl","Campeonatos":0,"pais":"Monaco"})


escuderias = db.get_collection('escuderias')
pilotos = db.get_collection('pilotos')

print([escuderiasInfo for escuderiasInfo in escuderias.find({},{"nombre":1,"Campeonatos":1})])

print([escuderiasInfo for escuderiasInfo in escuderias.find({},{"nombre":1,"Campeonatos":1}) if escuderias['nombre'] == 'AstonMartin'])

print([escuderiasInfo for escuderiasInfo in escuderias.find({"$or":[{"pilotos.pais":"España"},{"pilotos.pais":"Francia"}]},{"pilotos.nombre":1})])

print("####################")

print([escuderiasInfo for escuderiasInfo in escuderias.find({"$and":[{"Campeonatos":{"$lt":14}},{"pilotos.pais":"Inglaterra"}]})])

print([escuderiasInfo['nombre'] for escuderiasInfo in escuderias.find({"$and":[{"Campeonatos":{"$gte":4}},{"Campeonatos":{"$lte":14}}]})])
print("###################")
pipeline = [{'$lookup':{"from":'pilotos','localField':'pilotos','foreignField':'_id','as':'pilotos'}}]
print(list(escuderias.aggregate(pipeline)))

