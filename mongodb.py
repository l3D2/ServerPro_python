import pymongo as Mongo
class MongoDB:
    client = None
    Database = None
    def __init__(self, DB_NAME):
        self.client = Mongo.MongoClient("mongodb+srv://vatcharathon:oGZjEVNIm7OOPnAe@topgun.rudhxpv.mongodb.net/?retryWrites=true&w=majority")
        self.Database = self.client[DB_NAME]
        try:
            server_info = self.client.server_info()
            print("Connected to MongoDB successfully!")
            print(f"Server version: {server_info['version']}")
            print(f"Server status: {server_info['ok']}")
            print(f"Database: {DB_NAME}")
        except Mongo.errors.ConnectionFailure as e:
            print(f"Connection failed: {e}")
    def insertData(self, collection, data):
        col = self.Database[collection]
        result = col.insert_one(data)
        print(f"Inserted document ID: {result.inserted_id}")
    
    def updateData(self, collection, data):
        print("comming soon update")
    
    def deleteData(self, collection, data):
        col = self.Database[collection]
        result = col.delete_one(data)
        print(f"Deleted {result.deleted_count} document")
