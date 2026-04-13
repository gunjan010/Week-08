# 
# Filename: unittestdates.py
# Author: Nina Nyback
# date: 15 Oct 2025
# description: TestDate class
# This is all my own work as per the College's
# Academic Integrity Policy (copied from Moodle)
# 
import unittest
from dates import Date, DateOutOfRange

class TestDate(unittest.TestCase):
    def test_dates(self) -> None:
        dates = [(2020, 3, 14), (1972, 4, 23), (1996, 10, 4)]
        for date in dates:
            year = date[0]
            month = date[1]
            day = date[2]
            Date(year, month, day)
        return None
    def test_strings(self) -> None:
        dates = [(2020, 3, "14"), (1972, "4", 23), ("1996", 10, 4)]
        for date in dates:
            year = date[0]
            month = date[1]
            day = date[2]
            Date(year, month, day)
        
        
    def test_day_range(self) -> None:
        dates = [(2020, 3, -14), (1972, 4, 0), (1996, 10, 43)]
        for date in dates:
            year = date[0]
            month = date[1]
            day = date[2]
            with self.assertRaises(DateOutOfRange):
                Date(year, month, day)

        
    def test_month_range(self) -> None:
        dates = [(2020, 14, 14), (1972, -3, 23), (1996, 0, 4)]
        for date in dates:
            year = date[0]
            month = date[1]
            day = date[2]
            with self.assertRaises(DateOutOfRange):
                Date(year, month, day)

    def test_year_range(self) -> None:
        dates = [(-200, 3, 14), (0, 4, 23), (-2, 10, 4)]
        for date in dates:
            year = date[0]
            month = date[1]
            day = date[2]
            with self.assertRaises(DateOutOfRange):
                Date(year, month, day)

    def test_word_strings(self) -> None:
        dates = [("Twenty twenty", 3, 14), (1972, "four", 23), (1996, 10, "thirteen"),
                 (2020, "March", 14), (1972, "apr", 23), (1996, "OCT", 4)]
        for date in dates:
            year = date[0]
            month = date[1]
            day = date[2]
            with self.assertRaises(ValueError):
                Date(year, month, day)

unittest.main()
