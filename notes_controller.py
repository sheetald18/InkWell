from mongodb_connector import MongoConnect
import random
from datetime import datetime
mongo_connection=MongoConnect()
class Notes():
    def retrieve_note(self,note_id):
        try:
            note_details=mongo_connection.find_value('notes',{'note_id':note_id})

            return note_details,0
        except Exception as e:
            print(e)
            return e,1

    def retrieve_note_history(self,note_id):
        try:
            note_details=mongo_connection.find_history('notes',{'note_id':note_id})

            return note_details,0
        except Exception as e:
            print(e)
            return e,1
    def create_note(self, userid, note_details, noteid=None):
        try:
            if noteid==None:
                random_int=random.randint(0, 999999999)
                noteid=str(random_int).zfill(10)
            # note_details.update({}) 
            note_details.update({"updated_by":userid,"created_on":datetime.now(),"note_id":noteid})
            inserted_user_json=mongo_connection.insert_value('notes',note_details)

            if(inserted_user_json.acknowledged==False):
                return "Facing error. Please try again.",1
            return str(noteid),0
        except Exception as e:  
            print(e)
            return str(e),1
    
    def share_note(self, noteid, userids_list):
        try:
           
            inserted_user_json=mongo_connection.update_user_share_list(noteid,userids_list)
            print(inserted_user_json)
            if(inserted_user_json.acknowledged==False):
                return "Facing error. Please try again.",1
            return str(noteid),0
        except Exception as e:  
            print(e)
            return str(e),1
        
    def edit_note(self, userid,noteid, note, description):
        try:
            
            inserted_user_json=mongo_connection.insert_value('notes',{"note_id":noteid,"note":note,"description":description,"userids":"owner","created_by":userid, "created_on":datetime.now(),"shared_by":''})

            if(inserted_user_json.acknowledged==False):
                return "Facing error. Please try again.",1
            return str(noteid),0
        except Exception as e:  
            print(e)
            return str(e),1