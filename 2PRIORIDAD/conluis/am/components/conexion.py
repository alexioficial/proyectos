from pymongo import MongoClient

cluster = MongoClient('localhost', 27017)
db = cluster['am']

