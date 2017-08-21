import unittest

import sys
sys.path.append('../src')
import HelloWorld

class TestHelloWorld(unittest.TestCase):

    def testReturnIsCorrect(self):
        message = HelloWorld.helloWord()
        self.assertEqual(message, "Hello world!")

if __name__ == '__main__':
    unittest.main()
