import unittest
import leapyear

class testCaseAdd(unittest.TestCase):
    #test cases
    def test_leapyear1(self):
        #year divisible by 4
        self.assertEqual(leapyear.leapyear(24), True)

    
    


if __name__ == "__main__":
    unittest.main()
