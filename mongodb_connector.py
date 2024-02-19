from pymongo import MongoClient

class MongoConnect():

    
    def connect_mongo_db(self, db_name):
        try:
            connection=MongoClient()
            db_conn=connection[db_name]
            return db_conn
        except Exception as e:
            print(str(e))
            return None 
    def find_value(self,collection,key, value,retrieval_keys):
        try:
            db_conn=self.connect_mongo_db('inkwell')
            mongo_response=db_conn.get_collection(collection).find_one({key:value},retrieval_keys)
            return mongo_response
        except Exception as e:
            print(str(e))
            return None 