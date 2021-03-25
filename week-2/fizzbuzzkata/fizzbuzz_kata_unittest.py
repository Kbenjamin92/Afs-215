from fizzbuzz_kata import fizz_buzz_kata
import unittest   # The test framework

class Test_fizzbuzzkata(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizz_buzz_kata(1), 1)

    def test_fizzbuzzFunc(self):
        self.assertEqual(fizz_buzz_kata(2), 2)

    def test_divisible_by_three(self):
        self.assertEqual(fizz_buzz_kata(3), 'fizz')

    def test_divisible_by_five(self):
        self.assertEqual(fizz_buzz_kata(10), 'buzz')

    def test_divisible_by_three_and_five(self):
        self.assertEqual(fizz_buzz_kata(15), 'fizzbuzz')

if __name__ == '__main__':
    unittest.main()
