# import libs
import unittest

class HelloTestCase(unittest.TestCase):

    def setUp(self):
        self.greeting = 'Hello World!'

    def reverseString(self,msg):
        return msg[::-1]

    def testIhaveAVar(self):
        self.assertIsNotNone(self.greeting)
        self.assertTrue(self.greeting=='Hello World!', msg='This should say "Hello World!"')
        self.assertTrue('Hello' in self.greeting)

    def testThatICanReverseTheGreeting(self):
        self.assertTrue(self.greeting=='Hello World!', msg='This should say "Hello World!"')
        self.assertTrue(self.reverseString(self.greeting) == '!dlroW olleH')

d = HelloTestCase()
d.reverseString("hello")
