from mongodb_connector import MongoConnect
import random
from datetime import datetime
mongo_connection=MongoConnect()
class Notes():
    def retrieve_note(self,note_id,user_id):
        try:
            note_details=mongo_connection.retrieve_latest_note('notes',note_id,user_id)
            if(note_details==None):
                return "Please check noteid or userid",1
 
            return note_details,0
        except Exception as e:
            print(str(e))
            return e,1

    def retrieve_note_history(self,note_id,user_id):
        try:
            note_details=mongo_connection.find_history('notes',{'note_id':note_id,"userids":{"$in":[user_id]}})
            if note_details ==None:
                return ("There is no history for noteid: {0} and userid : {1}".format(note_id,user_id)),1
            return note_details,0
        except Exception as e:
            print(str(e))
            return str(e),1
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
            print(str(e))
            return str(e),1
    
    def share_note(self,user_id, noteid, userids_list):
        try:
           
            inserted_user_json=mongo_connection.update_user_share_list(user_id,noteid,userids_list)
            # print(inserted_user_json)
            if(inserted_user_json.modified_count==0):
                return "Please check userid / noteid. Please try again.",1
            return str(noteid),0
        except Exception as e:  
            print(str(e))
            return str(e),1
        