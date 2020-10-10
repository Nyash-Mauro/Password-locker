import random
import string

class User:
    '''Class that generate new instance of the user'''
    user_list = [] #empty user list

    def __init__(self,account_name,login_username,user_password):
        '''
        Initializing the var
        '''
        self.account_name = account_name
        self.login_username = login_username
        self.user_password = user_password

    def save_user(self):
        '''
        Method that saves user in the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        """
         method that deletes the saved user
        """
        User.user_list.delete(self)
    
    @classmethod
    def find_by_account_name(cls,account_name):
        """ 
        This method returns the user that matches the account name

        Args:
             account_name:value of the 
             acount_name to search for
        Returns:
             user that matches the acount_name
        """

        for user in cls.user_list:
            if user.account_name == account_name:
                return user


    @classmethod
    def user_exists(cls,login_username):
        """ 
        method that checks if the user exists from the list(user)
        Args:
            login_username:login_username to search if it exists
        Returns:True or false depending if the user exists in the list
        """
        for user in cls.user_list:
            if user.login_username == login_username:
                return True
            return False

    @classmethod
    def display_users(cls):
        """
         this mwthod returns user list 
        """
        return cls.user_list