import csv
import pymongo
from pymongo import MongoClient
from datetime import datetime
import sys
import bcrypt
sys.path.insert(0, '/opt/C3STEM/Middleware')

connection = MongoClient("mongodb://0.0.0.0:27017")
db = connection.c3stem_database

with open('/opt/C3STEM/DB/users.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	hashed_pass = bcrypt.hashpw(row[1].encode('utf-8'), bcrypt.gensalt())
    	db.student.update ({'_id' : row[0]}, {"$set": {'password' : hashed_pass}})
