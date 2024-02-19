from flask import Flask, request
app=Flask(__name__)
from validation_controller import Validation

validation_obj= Validation()
@app.route("/inkwell/test",methods=['GET'])
def testing():
    try:
        # print("tested successfully")
        return "tested successfuly"
    except Exception as e:
        print(e)
        return "error"

@app.route("/inkwell/login",methods=['POST'])
def login():
    try:
        from login_controller import Login
        login_obj= Login()
        request_inputs=request.json
        user_name=request_inputs['username']
        password=request_inputs['password']
        validation_msg, validation_status= validation_obj.validate_inputs_login_signup(user_name,password)
        if validation_status == 1 :
            return ({"message":validation_msg,"status_code":1}),400
        login_validation, login_status=login_obj.check_login_details(user_name,password)
        if login_status == 1:
            return ({"message":login_validation,"status_code":1}),401
        return ({"message":"Successfully Logged In","userid":login_validation,"status_code":0}),200
    except Exception as e:
        print(e)
        return ({"message":str(e),"status_code":0}),500

@app.route("/inkwell/signup",methods=['POST'])
def signup():
    try:
        from login_controller import Signup
        signup_obj= Signup()
        # validation_obj= Validation()
        request_inputs=request.json

        user_name=request_inputs['username']
        password=request_inputs['password']
        validation_msg, validation_status= validation_obj.validate_inputs_login_signup(user_name,password)
        
        if validation_status == 1 :
            return ({"message":validation_msg,"status_code":1}),400
        signup_validation, signup_status=signup_obj.signup_details(user_name,password)
        
        if signup_status == 1:
            return ({"message":signup_validation,"status_code":1}),401
        return ({"message":"Successfully Logged In","userid":signup_validation,"status_code":0}),200
    except Exception as e:
        print(e)
        return ({"message":str(e),"status_code":0}),500

@app.route("/inkwell/notes/create",methods=['POST'])
def create():
    try:
        from notes_controller import Notes
        notes_obj= Notes()
        request_inputs=request.json

        userid=request_inputs['userid']
        note=request_inputs['note']
        note_description=request_inputs['description']
        note_details={"note":note,"description":note_description,"userids":[userid],"created_by":userid}
        
        note_creation_response, note_creation_status=notes_obj.create_note(userid,note_details)
        
        if note_creation_status == 1:
            return ({"message":note_creation_response,"status_code":1}),401
        return ({"message":"Successfully Created Note","noteid":note_creation_response,"status_code":0}),200
    except Exception as e:
        print(e)
        return ({"message":str(e),"status_code":0}),500

@app.route("/inkwell/notes/share",methods=['POST'])
def share():
    try:
        from notes_controller import Notes
        notes_obj= Notes()
        request_inputs=request.json

        userid=request_inputs['userid']
        noteid=request_inputs['noteid']
        users_share_with=request_inputs['userid_list']
        # note_details={"note":note,"description":note_description,"userids":[userid],"created_by":userid}
        
        note_share_response, note_share_status=notes_obj.share_note(noteid,users_share_with)
        
        if note_share_status == 1:
            return ({"message":note_share_response,"status_code":1}),401
        return ({"message":"Successfully Shared Note","noteid":note_share_response,"status_code":0}),200
    except Exception as e:
        print(e)
        return ({"message":str(e),"status_code":0}),500

@app.route("/inkwell/notes/<noteid>",methods=['GET','PUT'])
def get_note(noteid):
    try:

        from notes_controller import Notes
        notes_obj= Notes()
        request_inputs=request.json


        user_id=request_inputs['userid']

        note_retrieval_response, note_retrieval_status=notes_obj.retrieve_note(noteid)
        print(note_retrieval_response)
        if note_retrieval_status == 1:
            return ({"message":note_retrieval_response,"status_code":1}),401
        
        if request.method == 'GET':
            return ({"message":"Successfully Retrived Note","note details":note_retrieval_response,"status_code":0}),200
        elif request.method == 'PUT':
            print("method is put")
            note=request_inputs['note']
            note_description=request_inputs['description']
            note_details={"note":note,"description":note_description,"userids":note_retrieval_response["userids"],"created_by":note_retrieval_response['created_by']}

            note_updation_response, note_updation_status=notes_obj.create_note(user_id,note_details,noteid)
            if note_updation_status == 1:
                return ({"message":note_updation_response,"status_code":1}),401
        
            return ({"message":"Successfully Updated Note","note details":note_updation_response,"status_code":0}),200

    
    except Exception as e:
        print(e)
        return ({"message":str(e),"status_code":0}),500

@app.route("/inkwell/notes/version_history/<noteid>",methods=['GET'])
def get_note_history(noteid):
    try:
        print(noteid)
        from notes_controller import Notes
        notes_obj= Notes()
        request_inputs=request.json

        user_id=request_inputs['userid']

        note_retrieval_response, note_retrieval_status=notes_obj.retrieve_note_history(noteid)
        print(note_retrieval_response)
        if note_retrieval_status == 1:
            return ({"message":note_retrieval_response,"status_code":1}),401
        return ({"message":"Successfully Retrived Note","note details":note_retrieval_response,"status_code":0}),200
    except Exception as e:
        print(e)
        return ({"message":str(e),"status_code":0}),500



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5100,debug=True)