from game import start


def login():
    print("-----------------------------------")
    print("Rock, Paper, Scissors Account Login")
    print("-----------------------------------")

    username = input("Please enter your username:   ")
    password = input("Please enter your password:   ")

    with open("accounts.csv") as f:
        if username and password in f.read():
            print("Access granted")
            start()

        else:
            print("Username or Password is wrong")
            login()
