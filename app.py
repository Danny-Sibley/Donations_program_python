from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}

donations = []

authorized_user = ""

total_donations = 0 


# enters while loop that terminates if 5 is chosen
while True:
    # invokes show_homepage function
    show_homepage()

    if not authorized_user:
        print("You must be logged in to donate")
    else:
        print("Logged in as ", authorized_user)
    #Catches incorrect input and asks user to retry 
    try:
        user_input = int(input("Please choose an option: "))
    except:
        print("Please enter a valid option.")
        continue 
    if user_input == 1:
        username = (input("Please enter username: ")).lower()
        password = input("Please enter password: ")
        authorized_user = login(database, username, password)
        continue

    elif user_input == 2:
        username = (input("Please enter username: ")).lower()
        password = input("Please enter password: ")
        #user_validation(username, password)
        authorized_user = register(database, username, password)
        if not authorized_user:
            database[username.lower()] = password
            continue

    elif user_input == 3:
        if not authorized_user:
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
            continue

    elif user_input == 4:
        show_donations(donations)
        continue
    
    elif user_input == 5:
        print("Goodbye")
        break
    else:
        print("Please choose a valid option.")