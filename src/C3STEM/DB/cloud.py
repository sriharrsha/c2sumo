import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

connection = MongoClient(os.getenv('MONGO_URI'))
db = connection.c3stem_database

ip = "X.X.X.X"
db.virtualmachine.insert({
    "_id": ip,
    "flavor": "m1.medium",
    "private_IP": 'X.X.X.X',
    "public_IP": ip,
    "key_name": "c3stem_keypair",
    "type": "TRANSIENT",
    "status": "AVAIL",
    "user": "ALL",
    "mode": "GROUP"
});   

ip = "X.X.X.X"
db.virtualmachine.insert({
    "_id": ip,
    "flavor": "m1.medium",
    "private_IP": 'X.X.X.X',
    "public_IP": ip,
    "key_name": "c3stem_keypair",
    "type": "TRANSIENT",
    "status": "AVAIL",
    "user": "ALL",
    "mode": "GROUP"
});
