import unittest

import sys
sys.path.append('../src')
import helloWorld

class TestHelloWorld(unittest.TestCase):

    def test_ReturnIsCorrect(self):
        message = helloWorld.helloWord()
        self.assertEqual(message, "Hello world!")

if __name__ == '__main__':
    unittest.main()
