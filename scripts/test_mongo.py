from pymongo import MongoClient

uri = "mongodb+srv://Rafly:raflymasuk@clustersaya.us0eloc.mongodb.net/?appName=Clustersaya"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)