import unittest
import fizzbuzz

class testCaseAdd(unittest.TestCase):
    #test cases
    def test_fizzbuzz1(self):
        #makes sure fizzbuzz creates an output of length 100
        self.assertEqual(len(fizzbuzz.fizzbuzz()),100)

    def test_fizzbuzz2(self):
        #tests that the 3rd position in the output array is "Fizz"
        self.assertEqual(fizzbuzz.fizzbuzz()[2], "Fizz")
    


if __name__ == "__main__":
    unittest.main()
