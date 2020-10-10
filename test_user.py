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

    def tearDown(self):
        """
        teardow method that cleans up after each test case has run
        """
        User.user_list = []

    def test_init(self):
        """
         test_init test case,to test if the new user is initialized well
        """
        self.assertEqual(self.new_user.account_name,"twitter")
        self.assertEqual(self.new_user.login_username,"Harnikovice")
        self.assertEqual(self.new_user.user_password,"nyash254")

    def test_save_user(self):
        """
        this test if the user is saved into the user list
        """
        self.new_user.save_user() #to save new user
        self.assertEqual(len(User.user_list),1)