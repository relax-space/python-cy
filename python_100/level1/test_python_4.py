import unittest
from python_4 import outputString


class Test_outputSting(unittest.TestCase):
    def setUp(self):
        self.obj = outputString('hello,world')
        self.str = self.obj.getString()

    def test_printString(self):
        self.assertEqual(self.obj.printString(),'HELLO,WORLD')


if __name__ == "__main__":
    unittest.main()