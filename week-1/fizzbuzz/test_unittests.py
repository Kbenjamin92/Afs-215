from fizzbuzzunittest import fizz_buzz   # The code to test
import unittest   # The test framework

class Test_TestFizz_buzz(unittest.TestCase):
    def test_fizz_one(self):
        self.assertEqual(fizz_buzz(1), '1')

    def test_fizz_two(self):
        self.assertEqual(fizz_buzz(2), '2')

if __name__ == '__main__':
    unittest.main()

