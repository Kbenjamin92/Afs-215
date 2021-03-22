from fizzbuzzunittest import fizz_buzz   # The code to test
import unittest   # The test framework

class Test_TestFizz_buzz(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(fizz_buzz(3), 'fizz')

    def test_fizz(self):
        self.assertEqual(fizz_buzz(1), 1)

if __name__ == '__main__':
    unittest.main()

