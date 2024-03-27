from pymongo import MongoClient

client=MongoClient("mongodb+srv://nitik1309:nitik1309@cluster0.jjl19zm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.registration

collection_name=db["registration_collections"]