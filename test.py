import unittest

class TestHello(unittest.TestCase):

  
    def test_hello(self):
        val = 2
        self.assertEqual(val, 2)

    def test_hello_hello(self):
        val = 2
        self.assertEqual(val, 2)

    def test_hello_name(self):
        val = 2
        self.assertEqual(val, 2)

if __name__ == '__main__':
    unittest.main()