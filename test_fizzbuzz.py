import unittest
import fizzbuzz

class testCaseAdd(unittest.TestCase):
    #test cases
    def test_fizzbuzz1(self):
        #makes sure fizzbuzz creates an output of length 100
        self.assertEqual(len(fizzbuzz.fizzbuzz()),100)
    


if __name__ == "__main__":
    unittest.main()
