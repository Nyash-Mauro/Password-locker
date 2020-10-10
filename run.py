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
