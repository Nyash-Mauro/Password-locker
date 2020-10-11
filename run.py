import random
from user import User


def create_user(account, username, password):
    """
    Function to create a new user for the list
    """
    new_user = User(account, username, password)
    return new_user


def save_user(user):
    """
    function to save the user
    """
    user.save_user()


def del_user(user):
    """
    function to delete the user
    """
    user.delete_user()


def find_user(account):
    """
    function that finds a user by username and returns the user credentials
    """
    return User.find_by_account_name(account)


def check_existing_user(username):
    """
    function to check if the user exists and returns a Boolean
    """
    return User.user_exists(username)


def display_users(account):
    """
    function that returns all the saved users
    """
    return User.display_users()


def user_exist(username, password):
    """
    function to chneck if the user exists
    """
    User.user_exists(username)
    return username


def main():
    print("")
    print("Hello !! Welcome to Password Locker.")
    while True:
        global username
        global account
        global password
        print("")
        print("-" * 50)
        print(
            "Use these codes to navigate:\n ca-Create an Account \n li-Log In \n ex-Exit"
        )
        short_code = input("Enter Your Choice:").lower().strip()
        if short_code == "ex":
            break

        # create an account print
        elif short_code == "ca":
            print("-" * 50)
            print("")
            print("To create a new account:")
            account = input("Enter your account -").strip()
            username = input("Enter your username -").strip()
            password = input("Enter your password -").strip()
            save_user(create_user(account, username, password))
            print("")
            print(
                f"New account Created for :{account} {username}using passcode:{password}"
            )
        elif short_code == "li":
            print("-" * 50)
            print("")
            print("To login,enter your user details :")
            account = input("Enter your acount account -")
            password = str(input("Enter your assword"))
            user_exists = (username(str), password)
            if user_exists == username:
                print(f"Welcome {username} .Choose an option to continue")
                print("")
                while True:
                    print("-" * 50)
                    print(
                        "Navigation codes: \n cc-Create Ur Creade \n dc-Display creade \n copy-Copy your password \n ex-exit"
                    )
                    psw_choise = input("Enter an option :").lower()
                    print("-" * 50)
                    if psw_choise == "ep":
                        print("")
                        password = input("Enter your password:")
                        break
                    elif psw_choise == "ex":
                        break
                    else:
                        print("Wrong option entered .Please try again")
                    save_user(create_user(account, username, password))
                    print("")
                    print(
                        f"User created:account name :{account} {username} password {password}"
                    )
                    print("")

        elif short_code == "dc":
            print("")
            if display_users(username):
                print("Here is a list of your credentials")
                print("")
                for user in display_users(account):
                    print(f"account: {account}-username:{username} password:{password}")
                    print("")
                else:
                    print("")
