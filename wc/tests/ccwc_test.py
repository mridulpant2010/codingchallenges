#how do you write a unit test case for the wordcount?
import unittest
from unittest.mock import patch
from src import WordCount

# class TestWordCount(unittest.TestCase):
#     @patch("wordcount.WordCount.word_count")
#     def test_word_count(self, mock_word_count):
#         mock_word_count.return_value = 1
#         wc = WordCount()
#         wc.word_count("test.txt")
#         mock_word_count.assert_called_once_with("test.txt")

#     @patch("wordcount.WordCount.line_count")
#     def test_line_count(self, mock_line_count):
#         mock_line_count.return_value = 1
#         wc = WordCount()
#         wc.line_count("test.txt")
#         mock_line_count.assert_called_once_with("test.txt")

wc = WordCount()
wc.word_count("../test.txt")
wc.byte_count("../test.txt")