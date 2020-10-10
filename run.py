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
        print("")
        print("-" * 60)
        print(
            "Use thes codes to navigate:\n ca-Create an Account \n li-Log In \n ex-Exit"
        )
        short_code = input("Enter Your Choice:").lower().strip()
        if short_code == "ex":
            break


# if __name__ == "__main__":
#     main()