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

    def test_save_multiple_user(self):
        """
        to check if we can save multiple user credentials to our user_list
        """
        self.new_user.save_user()
        test_user = User("Tiktok",
        "HarryMee","254juice")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
        """ 
        to check if one can delete the user from the list
        """
        self.new_user.save_user()
        test_user = User("youtube","justlaugh!","hahahaha") #new user credentials
        test_user.save_user()

        self.new_user.delete_user() #to delete the user credentials
        self.assertEqual(len(User.user_list),1)

    
    def test_find_user_by_account_name(self):
        """ 
        testg to check if we can find a user by acount name and display the data
        """
        self.new_user.save_user()
        test_user = User("twitter","Harnikovice","nyash254")
        test_user.save_user()
        found_user = User.find_by_acount_name("twitter")
        self.assertEqual(found_user.account_name,test_user.account_name)