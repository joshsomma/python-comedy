## import libs
import unittest

class emailTestCase(unittest.TestCase):

    def setUp(self):
        self.email_val = input('Give me an email address to check!')

    def checkEmail(self,test_email):
        return '@' in test_email

    def testForEmailForAtSymbol(self):
        # email_val = 'my.name@me.com'
        self.assertTrue(self.checkEmail(self.email_val),msg = 'no @ symbol present')

    def testForADotInTheEmail(self):
        x = split(self.email_val)





#e = emailTestCase()
#e.testCheckEmail('my.name@me.com')
