import pymongo

client = pymongo.MongoClient(
            "mongodb+srv://bosstimer:timerboss@cluster0.zxtp6.mongodb.net/Cluster0?retryWrites=true&w=majority")
conn = client["UUID"]
db = conn['uuids']



uuids = "03000200-0400-0500-0006-000700080009"

db.insert_one({uuids:"True","Akeneton":"Memoli"})
