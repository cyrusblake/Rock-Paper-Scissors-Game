from RPS_account_setup import setup
from RPS_account_login import login

print("To begin fill in the below information")

choice = input("Do you have an account? If yes type y. If no type n.    ")

while choice != "n" and choice != "N" and choice != "y" and choice != "Y":
    choice = input("Do you have an account? If yes type y. If no type n.    ")

if choice == "n" or choice == "N":
    setup()

if choice == "y" or choice == "Y":
    login()