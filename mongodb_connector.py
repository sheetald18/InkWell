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
    def find_value(self,collection,condition,retrieval_keys={}):
        try:
            db_conn=self.connect_mongo_db('inkwell')
            retrieval_keys.update({"_id":0})
            mongo_response=db_conn.get_collection(collection).find_one(condition,retrieval_keys)
            return mongo_response
        
        except Exception as e:
            print(str(e))
            return None 
    
    def find_history(self,collection,condition,retrieval_keys={}):
        try:
            db_conn=self.connect_mongo_db('inkwell')
            retrieval_keys.update({"_id":0})
            mongo_response=list(db_conn.get_collection(collection).find(condition,retrieval_keys))
            return mongo_response
        
        except Exception as e:
            print(str(e))
            return None 

    def insert_value(self,collection,values):
        try:
            db_conn=self.connect_mongo_db('inkwell')
            mongo_response=db_conn.get_collection(collection).insert_one(values)
            return mongo_response
        except Exception as e:
            print(str(e))
            return None 
    
    def update_user_share_list(self,noteid, users_list):
        try:
            db_conn=self.connect_mongo_db('inkwell')
            mongo_response=db_conn.get_collection('notes').update_many({"note_id":noteid},{"$push":{"userids":{"$each":users_list}}})
            print(mongo_response)
            return mongo_response
        except Exception as e:
            print(str(e))
            return None  
       