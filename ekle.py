import pymongo

client = pymongo.MongoClient(
            "mongodb+srv://bosstimer:timerboss@cluster0.zxtp6.mongodb.net/Cluster0?retryWrites=true&w=majority")
conn = client["UUID"]
db = conn['uuids']



uuids = "36444335-3431-4D33-4653-705A0F291754"

db.insert_one({uuids:"True"})
