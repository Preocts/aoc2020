"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day 4 part a

Because TDD is amazing and you should do it
"""
import unittest
from day04b import Passport_Validation_v2


class Test_Passports(unittest.TestCase):
    def test_birth(self):
        passport = Passport_Validation_v2()
        test = passport.check_birth
        self.assertFalse(test("1919"))
        self.assertFalse(test("2003"))
        self.assertFalse(test("asdf"))
        self.assertTrue(test("1920"))
        self.assertTrue(test("2002"))

    def test_issue(self):
        passport = Passport_Validation_v2()
        test = passport.check_issue
        self.assertFalse(test("1919"))
        self.assertFalse(test("2021"))
        self.assertFalse(test("asdf"))
        self.assertTrue(test("2010"))
        self.assertTrue(test("2020"))

    def test_expiry(self):
        passport = Passport_Validation_v2()
        test = passport.check_expiry
        self.assertFalse(test("1919"))
        self.assertFalse(test("2050"))
        self.assertFalse(test("asdf"))
        self.assertTrue(test("2020"))
        self.assertTrue(test("2030"))

    def test_height(self):
        passport = Passport_Validation_v2()
        test = passport.check_height
        self.assertFalse(test("190in"))
        self.assertFalse(test("190"))
        self.assertTrue(test("60in"))
        self.assertTrue(test("190cm"))

    def test_hair(self):
        passport = Passport_Validation_v2()
        test = passport.check_hair
        self.assertTrue(test("#123abc"))
        self.assertFalse(test("#123abz"))
        self.assertFalse(test("123abs"))

    def test_eye(self):
        passport = Passport_Validation_v2()
        test = passport.check_eye
        self.assertTrue(test("brn"))
        self.assertFalse(test("wat"))

    def test_id(self):
        passport = Passport_Validation_v2()
        test = passport.check_id
        self.assertTrue(test("000000001"))
        self.assertFalse(test("0123456789"))

    def test_cid(self):
        passport = Passport_Validation_v2()
        test = passport.check_cid
        self.assertTrue(test("Oh hi Mark."))
