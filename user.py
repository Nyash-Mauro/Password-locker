import random
import string

class User:
    '''Class that generate new instance of the user'''
    user_list = [] #empty user list

    def __init__(self,account_name,login_username,user_password):
        '''Initializing the var'''
        self.account_name = account_name
        self.login_username = login_username
        self.user_password = user_password

    def save_user(self):
        '''Method that saves user in the user_list'''
        User.user_list.append(self)

    def delete_user(self):
        """ method that deletes the saved user """
        User.user_list.delete(self)
    
    @classmethod
    def find_by_account_name(cls,account_name):
        