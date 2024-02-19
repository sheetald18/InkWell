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
