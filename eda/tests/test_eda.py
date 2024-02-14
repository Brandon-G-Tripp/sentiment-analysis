# from eda.nlp_sentiment_eda import calculate_review_lengths
import unittest

import sys

sys.path.append("../")


class TestEDA(unittest.TestCase):
    def test_import(self):
        # import nltk
        # import nltk.corpus
        self.assertTrue(True)

    # def test_review_lengths(self):
    #     lengths = calculate_review_lengths(...)

    #     self.assertEqual(len(lengths), 100)


if __name__ == "__main__":
    unittest.main()
