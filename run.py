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
    return User.user_