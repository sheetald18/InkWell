import re
class Validation():
    def validate_inputs_login_signup(self, username, password,email=None):
        try:
            pattern = '^[-_\.\w]+@([\w-]+\.)+[\w-]{2,4}$'
            # return re.match(pattern, email) is not None
            if (not isinstance(username, str) or username.strip() == ''):
                return "Please enter proper username" , 1
            if (not isinstance(password, str) or password.strip() == ''):
                return "Please enter proper password" , 1

            if (email !=None and (not isinstance(email, str) or re.match(pattern,email)==None)):
                return "Please enter proper email address" , 1
            return "successfully validated username and password" ,0 
        except Exception as e:
            print(str(e))
            return str(e),1
    
    def validate_inputs_notes(self, note, description):
        try:

            if (not isinstance(note, str) or note.strip() == ''):
                return "Please enter proper note" , 1
            if (not isinstance(description, str) or description.strip() == ''):
                return "Please enter proper description" , 1

            return "successfully validated note and description" ,0 
        except Exception as e:
            print(str(e))
            return str(e),1