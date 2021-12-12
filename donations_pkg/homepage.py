def show_homepage():
    print("        === Donate Homepage ===      ")
    print("-------------------------------------------")
    print("| 1.    Login    | 2.    Register          |")
    print("-------------------------------------------")
    print("| 3.    Donate   | 4.    Show Donations    |")
    print("-------------------------------------------")
    print("| 5.    Exit                               |")
    print("-------------------------------------------")


def donate(username):
    try:
        donation_amt = float(input("Enter amount to donate: "))
    except ValueError:
        print("Please enter a number.")
        return
    if donation_amt <= 0:
        print("Please enter a number greater than 0.")
    else:
        donation = (f'{username} donated ${ donation_amt}')
        print("Thank you for the donation!")
        return donation


def show_donations(donations):
    total_donations = 0
    print("\n--- All Donations ---")
    if donations == []:
        print("There are no donations currently.")
    else:
        for donation in donations:
            print(donation)
            #total_donations += donation
