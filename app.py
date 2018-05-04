from pymongo import MongoClient
#import requests


client = MongoClient("mongodb://localhost:27017")
db=client.products
collection=db.DeploymentType
cursor=db.DeploymentType.find()

for document in cursor:
    print(document)

##requests=requests.get("http://ya.ru")

##print(requests.content)
