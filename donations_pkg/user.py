def login(database, username, password):
    # if username_length >10:
    #     print ("Username needs to be less than 10 characters.")
    if username in database.keys() and database[username] == password:
        print("Welcome back ", username, "!")
        return username
    elif username in database.keys() and database[username] != password:
        print("Incorrect password")
        return ""
    else:
        print("Username not found")
        return ""


def register(database, username, password):
    if len(password) < 5 and len(username) > 10:
        print("Username needs to be less than 10 characters.")
        print("password must be atleast 5 characters.")
        return ""
    elif len(password) < 5:
        print("password must be atleast 5 characters.")
        return ""
    elif len(username) > 10:
        print("Username needs to be less than 10 characters.")
        return ""
    else:
        if username.lower() in database.keys():
            print(username, " is already registered.")
            return ""
        else:
            print(username, "has has been registered.")
            return username


"""
def user_validation(username,password):
    if len(password) <5 and len(username) >10:
        print("Username needs to be less than 10 characters.")
        print("password must be atleast 5 characters.")
    elif len(password) <5:
        print("password must be atleast 5 characters.")
    elif len(username) >10:
        print("Username needs to be less than 10 characters.")
    elif len(username) >10 and len(password) <5:
    
"""
