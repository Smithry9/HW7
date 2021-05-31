import unittest
import leapyear

class testCaseAdd(unittest.TestCase):
    #test cases
    def test_leapyear1(self):
        #year divisible by 4
        self.assertEqual(leapyear.leapyear(24), True)

    def test_leapyear2(self):
        #year divisible by 200
        self.assertEqual(leapyear.leapyear(200), False)

    
    


if __name__ == "__main__":
    unittest.main()
