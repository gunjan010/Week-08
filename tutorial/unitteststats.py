# 
# Filename: unitteststats.py
# Author: Nina Nyback
# date: 15 Oct 2025
# description: TestStats class
# This is all my own work as per the College's
# Academic Integrity Policy (copied from Moodle)
# 
import unittest
from stats import Statistics

class TestStats(unittest.TestCase):
    def setUp(self) -> None:
        #setup values to reuse
        self.count = 3
        self.means = [3, 2.5, 3]
        self.medians = [3, 2.5, 2]    # passes the tests
        # fails the test self.medians = [2, 2.5, 3]

        # Statistics objects to use to test success
        self.stats_to_pass = [
            Statistics([3, 2, 4]),
            Statistics([3, 2, 4, 1]),
            Statistics([3, 2, 4, 1, 5])
        ]

        # Statistics objects to use to test exceptions when failing
        self.stats_to_fail = [
            Statistics([3, 2, 4, 2]),
            Statistics([3, 2, 2]),
            Statistics([3, 2, 3])
        ]
    def test_mean_pass(self) -> None:
        for index in range(0, self.count):
            #get the mean of each Stats object
            actual_mean = self.stats_to_pass[index].mean()
            #get the expected mean for each Stats object
            expected_mean = self.means[index]
            # the means should be identical
            # use assertEqual
            self.assertEqual(actual_mean, expected_mean)
        return None
    
    def test_mean_fail(self) -> None:
        for index in range(self.count):
            # get the actual mean of each Stats object
            actual_mean = self.stats_to_fail[index].mean()
            # get the expected mean for each Stats object
            expected_mean = self.means[index]
            # the means should be different
            # use assertNotEqual
            self.assertNotEqual(actual_mean, expected_mean)
        return None
    
    def test_median_pass(self) -> None:
        for index in range(self.count):
            # get the actual median for each Stats object
            actual_median = self.stats_to_pass[index].median()
            # get the expected median for each Stats object
            expected_median = self.medians[index]
            # the means should be identical
            # use assertEqual
            self.assertEqual(actual_median, expected_median)
        return None
    
    def test_median_fail(self) -> None:
        for index in range(self.count):
            # get the actual median of each Stats object
            actual_median = self.stats_to_fail[index].median()
            # get the expected median
            expected_median = self.medians[index]
            # the means should be different
            # use assertNotEqual
            self.assertNotEqual(actual_median, expected_median)
        return None
    
    def test_append(self) -> NOne:
        for stats in self.stats_to_pass:
            # initial length of each stats
            initial_length = stats.length()
            stats.append(4)
            # new length
            new_length = stats.length()
            # initial length should be less than new length
            self.assertLess(initial_length, new_length)
            # alternatively, new length should be greater than initial length
    
    def test_remove_pass(self) -> None:
        for stats in self.stats_to_pass:
            # initial length of each stats
            initial_length = stats.length()
            stats.remove(3)
            # new length
            new_length = stats.length()
            # new length should be greater than initial length
            self.assertGreater(initial_length, new_length)
    
    def test_remove_fail(self) -> None:
        #for stats in self.stats_to_fail:  ??????????????????
            for stats in self.stats_to_fail:
                # excepts exceptions
                with self.assertRaises(ValueError):
                    stats.remove(5) # exception should be raised

unittest.main()  # runs test code
