import unittest #importing unittest from python
from user import User #importing class user

class TestUser(unittest.TestCase):
    """
     This test defines test cases for user class behaviors

     Args:
          unittest.TestCase: TestCase that aids in creating test cases
    """

    def setUp(self):
        """ 
        this method to run before each test cases
        """

        self.new_user = User("twitter","Harnikovice","nyash254") #create a new user

    def