#!/usr/bin/env python3

import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_luhn_verified(self):
        self.assertEqual("Authentic", utils.luhn_verified('5558397375275489'))
        self.assertEqual("Authentic", utils.luhn_verified('4573055613536303098'))
        self.assertEqual("Fake", utils.luhn_verified('5558397375275488'))
        self.assertEqual("Fake", utils.luhn_verified('4573055613536303099'))

    def test_is_valid(self):
        self.assertTrue(utils.is_valid('5558397375275489'))
        self.assertTrue(utils.is_valid('4573055613536303098'))
        self.assertFalse(utils.is_valid('abc'))
        self.assertFalse(utils.is_valid(''))
        self.assertFalse(utils.is_valid('!'))
        self.assertFalse(utils.is_valid('abc123'))
