from RPS_account_login import login


def setup():
    print("-----------------------------------")
    print("Rock, Paper, Scissors Account Setup")
    print("-----------------------------------")

    username = input("Pick a username:  ")
    password = input("Pick a password:  ")

    with open("accounts.csv") as f:
        if username in f.read():
            print("Username already exist")
            setup()

    password_confirm = input("Please confirm your password: ")
    if password == password_confirm:
        print("Your Account has been setup.")
        text_file = open("accounts.csv", "a")
        text_file.write(username)
        text_file.write(" , ")
        text_file.write(password)
        text_file.write("\n" * 2)
        text_file.close()
        login()
    elif password != password_confirm:
        print("Your password don't match. Please try again.")
        if password != password_confirm:
            setup()
