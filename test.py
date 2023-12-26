"""
Energy Core	
Gryphon	
Nipar Bridge	
Pathos	
Prog. Military Base	
Quetzalcoatl	
Shrine	
Hornian King	
Hornian Queen	
Messenger	
Mountain Sage	
Control Tower	
Egma Schill	
Gigantic God	
Ordin	
Rock Emperor	
Skadi	
Black Widow	
Echelon	
Bishop Black	
Bishop Blue	
Bishop Green	
Bishop Orange	
Bishop Rainbow	
Bishop Red	
Guardian of Vatallus	
RM-230	
Sekhmete
"""


dict_ = {
    "Energy Core": "0000/00/00_00:00:00",
    "Gryphon": "0000/00/00_00:00:00",
    "Nipar Bridge": "0000/00/00_00:00:00",
    "Pathos": "0000/00/00_00:00:00",
    "Prog. Military Base": "0000/00/00_00:00:00",
    "Quetzalcoatl": "0000/00/00_00:00:00",
    "Shrine": "0000/00/00_00:00:00",
    "Hornian King": "0000/00/00_00:00:00",
    "Hornian Queen": "0000/00/00_00:00:00",
    "Messenger": "0000/00/00_00:00:00",
    "Mountain Sage": "0000/00/00_00:00:00",
    "Control Tower": "0000/00/00_00:00:00",
    "Egma Schill": "0000/00/00_00:00:00",   
    "Gigantic God": "0000/00/00_00:00:00",
    "Ordin": "0000/00/00_00:00:00",
    "Rock Emperor": "0000/00/00_00:00:00",
    "Skadi": "0000/00/00_00:00:00",
    "Black Widow": "0000/00/00_00:00:00",
    "Echelon": "0000/00/00_00:00:00",
    "Bishop Black": "0000/00/00_00:00:00",
    "Bishop Blue": "0000/00/00_00:00:00",
    "Bishop Green": "0000/00/00_00:00:00",
    "Bishop Orange": "0000/00/00_00:00:00",
    "Bishop Rainbow": "0000/00/00_00:00:00",
    "Bishop Red": "0000/00/00_00:00:00",
    "Guardian of Vatallus": "0000/00/00_00:00:00",
    "RM-230": "0000/00/00_00:00:00",
    "Sekhmete": "0000/00/00_00:00:00"
}



"""
username : ercansezdizero
password : gSYctsmB1GRcSjjd

"""
from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://ercansezdizero:gSYctsmB1GRcSjjd@cluster0.yvcr1u2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client["galaxyrivals"]
collection = db["bosses"]


# collection.insert_one(dict_)



#veri isteme 

for i in collection.find():
    print(i)
# 
#update all
# collection.update_many({},{"$set":{"date":"0000/00/00_00:00:00"}}) // last update

    


