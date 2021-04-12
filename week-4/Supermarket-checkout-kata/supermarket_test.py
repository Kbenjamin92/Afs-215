import unittest   
from supermarketcheckout import Checkout

class Test_Class(unittest.TestCase):
    def test(self):
        self.testClass = Checkout()

    def test_isInstance(self):        
        message = "The object is not instance of Checkout."
        self.assertIsInstance(self.testClass, Checkout, message)  

    def test_shop(self):
        self.assertIsInstance(self.testClass.shop(), Checkout)
