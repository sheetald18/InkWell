from mongodb_connector import MongoConnect
mongo_connection=MongoConnect()
class Login():
    def validate_inputs(self, username, password):
        try: 
            if (not isinstance(username, str) or username.strip() == ''):
                return "Please enter proper username" , 1
            if (not isinstance(password, str) or password.strip() == ''):
                return "Please enter proper password" , 1
            return "successfully validated username and password" ,0 
        except Exception as e:
            print(str(e))
            return str(e),1
    
    def check_login_details(self, username, password):
        try:
            # db_conn=mongo_connection.connect_mongo_db("inkwell")
            # present_user_json=db_conn.get_collection("users").find_one({"username":username},{"userid":1, "password":1})
            present_user_json=mongo_connection.find_value('users','username',username,{"userid":1, "password":1})
            print(present_user_json)
            if(present_user_json==None):
                return "Invalid username. Please sign up",1
            if present_user_json['password']!=password:
               return "Invalid password. Please check the password",1 
            return present_user_json['userid'],0
        except Exception as e:
            print(e)
            return str(e),1