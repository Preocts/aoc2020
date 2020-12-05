"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day05
"""
import unittest

import day05a


class TestBoardingPasses(unittest.TestCase):
    """ Boarding Pass is a seating location in Binary Code """

    def setUp(self):
        self.target = day05a.BoardingPass()

    def test_attributes(self):
        """ Class API health """
        self.assertTrue(hasattr(self.target, "set_boarding_pass"))
        self.assertTrue(hasattr(self.target, "get_row"))
        self.assertTrue(hasattr(self.target, "get_column"))
        self.assertTrue(hasattr(self.target, "get_id"))

    def test_setting_value(self):
        """ Accept valid boarding pass data only """
        self.target.set_boarding_pass("FFFFFFFRRR")
        self.assertEqual(str(self.target), "FFFFFFFRRR")
        self.assertTrue(self.target)

        self.target.set_boarding_pass("FFFFFFRRR")
        self.assertEqual(str(self.target), "")
        self.assertFalse(self.target)

        self.target.set_boarding_pass("invalid")
        with self.assertRaises(Exception):
            self.target.get_row()

    def test_get_row(self):
        """ Get the seat location by row """
        self.target.set_boarding_pass("FBFBBFFRLR")
        self.assertEqual(self.target.get_row(), 44)

        self.target.set_boarding_pass("BFFFBBFRRR")
        self.assertEqual(self.target.get_row(), 70)

        self.target.set_boarding_pass("FFFBBBFRRR")
        self.assertEqual(self.target.get_row(), 14)

        self.target.set_boarding_pass("BBFFBBFRLL")
        self.assertEqual(self.target.get_row(), 102)

    def test_get_column(self):
        """ Get the seat location by column """
        self.target.set_boarding_pass("FBFBBFFRLR")
        self.assertEqual(self.target.get_column(), 5)

        self.target.set_boarding_pass("BFFFBBFRRR")
        self.assertEqual(self.target.get_column(), 7)

        self.target.set_boarding_pass("FFFBBBFRRR")
        self.assertEqual(self.target.get_column(), 7)

        self.target.set_boarding_pass("BBFFBBFRLL")
        self.assertEqual(self.target.get_column(), 4)

    def test_seat_id(self):
        self.target.set_boarding_pass("FBFBBFFRLR")
        self.assertAlmostEqual(self.target.get_id(), 357)

        self.target.set_boarding_pass("BFFFBBFRRR")
        self.assertAlmostEqual(self.target.get_id(), 567)

        self.target.set_boarding_pass("FFFBBBFRRR")
        self.assertAlmostEqual(self.target.get_id(), 119)

        self.target.set_boarding_pass("BBFFBBFRLL")
        self.assertAlmostEqual(self.target.get_id(), 820)

    def test_pass_validate(self):
        """ Ensure input string is valid """
        self.assertTrue(self.target.pass_validate("FBFBFBFLRL"))
        self.assertFalse(self.target.pass_validate("FBFBFBFBRL"))
        self.assertFalse(self.target.pass_validate("FBFBFbFLRL"))
