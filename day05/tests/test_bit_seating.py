"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day day05
"""
import unittest

import day05


class TestBoardingPasses(unittest.TestCase):
    """ Boarding Pass is a seating location in Binary Code """

    def setUp(self):
        self.target = day05.BoardingPass()

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


class TestSeatingChart(unittest.TestCase):
    """ Make sure your plane is not over-filled today!"""

    def setUp(self):
        self.target = day05.SeatingChart()

    def test_attributes(self):
        """ Health check of class """
        self.assertTrue(hasattr(self.target, "_generate_chart"))
        self.assertTrue(hasattr(self.target, "load_used_ids"))
        self.assertTrue(hasattr(self.target, "remaining_ids"))

    def test_generate_seats(self):
        expected = (0, 1, 2, 3, 4, 5, 6, 7, )
        self.assertEqual(self.target._generate_chart(0, 1), expected)

    def test_load_used_ids(self):
        mocklist = [0, 1, 2, 3, 4, 5, 6, 7, ]
        self.assertTrue(self.target.load_used_ids(mocklist))

        self.assertEqual(self.target.used_ids, tuple(mocklist))

    def test_remaining_ids(self):
        mocklist = [0, 1, 2, 3, 4, 5, 6, ]
        self.target.load_used_ids(mocklist)
        self.assertEqual(self.target.remaining_ids(0, 1), (7, ))
