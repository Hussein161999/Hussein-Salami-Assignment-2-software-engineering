"""
Unit tests for the Scrabble score computation and word validation functions.
"""
import unittest
from scrabble_score import compute_score, is_valid_word


class TestScrabbleScore(unittest.TestCase):
    """Tests for Scrabble score and word validation."""

    def test_compute_score(self):
        """Test Scrabble score computation."""
        self.assertEqual(compute_score("cabbage"), 14)
        self.assertEqual(compute_score("CABBAGE"), 14)
        self.assertEqual(compute_score("a"), 1)
        self.assertEqual(compute_score("z"), 10)
        self.assertEqual(compute_score(""), 0)

    def test_is_valid_word(self):
        """Test word validation against dictionary."""
        dictionary = {"apple", "banana", "cabbage", "dog"}
        self.assertTrue(is_valid_word("apple", dictionary))
        self.assertFalse(is_valid_word("xyz", dictionary))
        self.assertTrue(is_valid_word("APPLE", dictionary))
        self.assertFalse(is_valid_word(" ", dictionary))


if __name__ == "__main__":
    unittest.main()
