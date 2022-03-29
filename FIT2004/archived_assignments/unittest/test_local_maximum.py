import unittest
import os
import inspect
import sys

sys.path.insert(0, "/Users/rubber/University-notes/FIT2004/assignments/")
import local_max as lm

class test_wordle(unittest.TestCase):
    def setUp(self):
        pass

    def test_lm1(self):
        arr=[[1,2,27,28,29,30,49],[3,4,25,26,31,32,48],[5,6,23,24,33,34,47],[7,8,21,22,35,36,46],[9,10,19,20,37,38,45],[11,12,17,18,39,40,44],[13,14,15,16,41,42,43]]

        result = lm.find_local_max(arr)
        expected = [0, 6]

        self.assertEqual(result, expected)


    def test_lm2(self):
        arr = [[1,3,6,10,15,21,28], [2,5,9,14,20,27,34], [4,8,13,19,26,33,39],[7,12,18,25,32,38,90],[11,17,24,31,37,57,91],[99,98,97,60,59,58,56], [22,29,35,40,44,55,49]]

        result = lm.find_local_max(arr,)
        expected = [[5, 0], [4, 6]]

        self.assertIn(result,expected)


    def test_lm3(self):
        arr= [[1,3,6,10,15,21,28],[2,5,9,14,20,27,34],[4,8,13,19,50,33,39],[7,12,18,25,32,38,51], [52,17,24,31,37,42,46],[16,23,30,36,41,45,48],[22,29,35,40,44,47,49]]

        result = lm.find_local_max(arr,)
        expected = [[2,4], [3, 6], [4, 0], [6,6]]
        result = lm.find_local_max(arr,)

        self.assertIn(result,expected)

    def test_lm4(self):
        arr= [[1,3,6,10,15,21,28],[2,5,9,14,20,27,34],[4,8,13,19,0,33,39],[7,12,18,25,32,38,51], [0,17,24,31,37,42,46],[16,23,30,36,41,45,48],[22,29,35,40,44,47,0]]

        result = lm.find_local_max(arr,)
        expected = [[3, 6]]
        result = lm.find_local_max(arr,)

        self.assertIn(result,expected)


    def test_lm5(self):
        # arr= [[1,3,6,10,15,21,0],[2,5,9,14,20,27,0],[4,8,13,19,0,33,0],[7,12,18,25,32,38,0], [52,17,24,31,37,42,46],[16,23,30,36,41,45,48],[22,29,35,40,44,47,0]]
        arr= [[1,3,6,10,15,21,28],[2,5,9,14,20,27,34],[4,8,13,19,50,33,39],[7,12,18,25,32,38,51], [52,17,24,31,37,42,46],[16,23,30,36,41,45,48],[22,29,35,40,44,47,49]]
        result = lm.find_local_max(arr,)
        expected = [[4,0], [2, 4], [3, 6], [6, 6]]
        result = lm.find_local_max(arr,)

        self.assertIn(result,expected)


def main():
    # Create a test suit
    suit = unittest.TestLoader().loadTestsFromTestCase(test_wordle)
    # Run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)



main()
