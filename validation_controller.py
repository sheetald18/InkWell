class Validation():
    def validate_inputs_login_signup(self, username, password):
        try: 
            if (not isinstance(username, str) or username.strip() == ''):
                return "Please enter proper username" , 1
            if (not isinstance(password, str) or password.strip() == ''):
                return "Please enter proper password" , 1
            return "successfully validated username and password" ,0 
        except Exception as e:
            print(str(e))
            return str(e),1