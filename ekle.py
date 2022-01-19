import pymongo

client = pymongo.MongoClient(
            "mongodb+srv://bosstimer:timerboss@cluster0.zxtp6.mongodb.net/Cluster0?retryWrites=true&w=majority")
conn = client["UUID"]
db = conn['uuids']



uuids = "DD24D3B0-C533-4760-A447-0203007BE85B"

db.insert_one({uuids:"True","test":"test"})
