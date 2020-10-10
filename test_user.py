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
        this method to run bef
        """