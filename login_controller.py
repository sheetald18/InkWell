from mongodb_connector import MongoConnect
mongo_connection=MongoConnect()
import random
class Login():
    
    
    def check_login_details(self, username, password):
        try:
            present_user_json=mongo_connection.find_value('users',{'username':username},{"userid":1, "password":1})
            # print(present_user_json)
            if(present_user_json==None):
                return "Invalid username. Please sign up",1
            if present_user_json['password']!=password:
               return "Invalid password. Please check the password",1 
            return present_user_json['userid'],0
        except Exception as e:
            print(e)
            return str(e),1
        
class Signup():
    def signup_details(self, username, password):
        try:
            random_int=random.randint(0, 99999)
            userid=username[:3]+str(random_int).zfill(5)
            # print(userid)
            inserted_user_json=mongo_connection.insert_value('users',{"userid":userid,"username":username, "password":password})
            # print(inserted_user_json.inserted_id)
            if(inserted_user_json.acknowledged==False):
                return "Facing error. Please sign up again",1
            return str(userid),0
        except Exception as e:  
            print(e)
            return str(e),1