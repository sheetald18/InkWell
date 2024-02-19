from flask import Flask, request
app=Flask(__name__)

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
        validation_msg, validation_status= login_obj.validate_inputs(user_name,password)
        if validation_status == 1 :
            return ({"message":validation_msg,"status_code":1}),400
        login_validation, login_status=login_obj.check_login_details(user_name,password)
        if login_status == 1:
            return ({"message":login_validation,"status_code":1}),401
        return ({"message":login_validation,"status_code":0}),200
    except Exception as e:
        print(e)
        return ({"message":login_validation,"status_code":0}),500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5100,debug=True)