import unittest
import os
import inspect
import sys

sys.path.insert(0, "/Users/rubber/University-notes/FIT2004/assignments/")
import wordle as wordle

class test_wordle(unittest.TestCase):
    def test_count(self):
        count_string = "aabbccz"
        testcase = wordle.count(count_string)
        correct = [0] * 26
        correct[0] = correct[1] = correct[2] = 2
        correct[-1] = 1
        print("The correct result for count of", count_string, "is", correct)
        self.assertEqual(testcase, correct)


    def setUp(self):
        self.wordlist = ['limes', 'spare', 'store', 'loser', 'aster', 'pares', 'taser', 'pears', 'stare', 'spear', 'parse', 'reaps', 'rates', 'tears', 'losts']

    def test_wordle1(self):
        word = 'pares'
        marker = [0,0,0,0,1]
        expected = ['reaps']
        result = wordle.trainer(self.wordlist, word, marker)
        self.assertEqual(result, expected)


    def test_wordle2(self):
        # the wordlist input

        word = 'pares'
        marker = [1, 0, 0, 0, 1]
        result = wordle.trainer(self.wordlist, word, marker)
        expected = ['pears']
        self.assertEqual(result, expected)


    def test_wordle_two_output(self):

        # The guessed word
        word = 'pares'
        # The markers based on the guessed word
        marker = [0, 0, 0, 0, 0]
        result = wordle.trainer(self.wordlist, word, marker)
        expected = ['spare', 'spear']
        self.assertEqual(result, expected)


    def test_wordle_empty_output(self):
        # Example 04
        # The wordlist input

        # The guessed word
        word = 'spare'
        # The markers based on the guessed word
        marker = [1, 1, 0, 0, 1]
        result = wordle.trainer(self.wordlist, word, marker)
        expected = []
        self.assertEqual(result, expected)


    def test_wordle3(self):
        # The wordlist input

        # The guessed word
        word = 'sprae'
        # The markers based on the guessed word
        marker = [1, 1, 0, 0, 1]
        result = wordle.trainer(self.wordlist, word, marker)
        expected = ['spare']
        self.assertEqual(result, expected)


    def test_wordle_inside_wordlist(self):
        # Example 06
        # The wordlist input

        # The guessed word
        word = 'spare'
        # The markers based on the guessed word
        marker = [1, 1, 1, 1, 1]
        result = wordle.trainer(self.wordlist, word, marker)
        expected = ['spare']
        self.assertEqual(result, expected)


    def test_wordle4(self):
        # Example 07
        # The word
        wordlist = ['costar', 'carets', 'recast', 'traces', 'reacts', 'caster', 'caters', 'crates', 'actors', 'castor']
        word = 'catrse'
        # The markers based on the guessed word
        marker = [1, 1, 0, 0, 0, 0]
        result = wordle.trainer(wordlist, word, marker)
        expected = ['carets', 'caster']
        self.assertEqual(result, expected)

def main():
    # Create a test suit
    suit = unittest.TestLoader().loadTestsFromTestCase(test_wordle)
    # Run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)



main()

