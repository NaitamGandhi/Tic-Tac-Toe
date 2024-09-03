"""
Unmocked unit testing
"""
import os
import sys
import unittest
sys.path.append(os.path.abspath('../../'))
from app import check_table
from app import get_leaderboard

USERNAME_INPUT = "username"
EXPECTED_OUTPUT = "exists"

class CheckTable(unittest.TestCase):
    """This tests to see if the check_table fucntion can detects a new user vs. persisted user"""
    def setUp(self):
        self.check_table_test_params = [
            {
                USERNAME_INPUT: "naitam", # already in table
                EXPECTED_OUTPUT: True
            },
            {
                USERNAME_INPUT: "obama", # already in table
                EXPECTED_OUTPUT: True
            },
            {
                USERNAME_INPUT: "someone new", # not in table
                EXPECTED_OUTPUT: False
            },
            {
                USERNAME_INPUT: "another new person", # not in table
                EXPECTED_OUTPUT: False
            }
        ]

    def test_check_table(self):
        """This tests the check_table function"""
        count = 0
        for test in self.check_table_test_params:
            # then assign it to a variable
            actual_result = check_table(test[USERNAME_INPUT])
            # Assign the expected output as a variable from test
            expected_result = test[EXPECTED_OUTPUT]

            # Use assert checks to see compare values of the results
            self.assertEqual(actual_result, expected_result)

            if count in (0, 1): # check the first two only
                self.assertTrue(actual_result, expected_result)

            if count in (2, 3): # check the last two only
                self.assertFalse(actual_result, expected_result)
            count += 1

INPUT = "new"
EXPECTED_LEADERBOARD = "updated"

class GetLeaderboard(unittest.TestCase):
    """See if players and their score are appending in the dictionary and getting copied from db table"""
    # the tested value will not be sorted nor persisted nor check for duplicates
    def setUp(self):
        self.get_leaderboard_test_params = [
            {
                INPUT: {
                    "players": [],
                    "score": []
                },
                EXPECTED_LEADERBOARD: { # the persisted table that's already in db
                    "players": ['naitam', 'op', 'user4', 'here2', 'newnewnew', 'newone', ' user4', 'user3', 'One person', 'There', 'naiam', 'newnew', 'user', 'onemore', 'newUser', 'there', 'obama', 'user2', 'here'],
                    "score": [117, 102, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 98, 97, 96, 91]
                }
            },
            {
                INPUT: { # check to see if a unique name and score are added
                    "players": ['new guy'],
                    "score": [100]
                },
                EXPECTED_LEADERBOARD: {
                    "players": ['new guy', 'naitam', 'op', 'user4', 'here2', 'newnewnew', 'newone', ' user4', 'user3', 'One person', 'There', 'naiam', 'newnew', 'user', 'onemore', 'newUser', 'there', 'obama', 'user2', 'here'],
                    "score": [100, 117, 102, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 98, 97, 96, 91]
                }
            },
            {
                INPUT: { # check to see if a duplicate username can be added
                    "players": ['naitam'],
                    "score": [1002]
                },
                EXPECTED_LEADERBOARD: {
                    "players": ['naitam', 'naitam', 'op', 'user4', 'here2', 'newnewnew', 'newone', ' user4', 'user3', 'One person', 'There', 'naiam', 'newnew', 'user', 'onemore', 'newUser', 'there', 'obama', 'user2', 'here'],
                    "score": [1002, 117, 102, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 98, 97, 96, 91]
                }
            },
            {
                INPUT: { # check to see if an exact user and score can be added
                    "players": ['naitam'],
                    "score": [117]
                },
                EXPECTED_LEADERBOARD: {
                    "players": ['naitam', 'naitam', 'op', 'user4', 'here2', 'newnewnew', 'newone', ' user4', 'user3', 'One person', 'There', 'naiam', 'newnew', 'user', 'onemore', 'newUser', 'there', 'obama', 'user2', 'here'],
                    "score": [117, 117, 102, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 98, 97, 96, 91]
                }
            },
        ]

    def test_get_leaderboard(self):
        """This tests the get_leaderboard function"""
        for test in self.get_leaderboard_test_params:
            # then assign it to a variable
            actual_result = get_leaderboard(test[INPUT])
            # Assign the expected output as a variable from test
            expected_result = test[EXPECTED_LEADERBOARD]
            # Use assert checks to see compare values of the results
            self.assertEqual(actual_result, expected_result)
            self.assertIsNot(actual_result["players"], expected_result["players"])
            self.assertIsNot(actual_result["score"], expected_result["score"])

if __name__ == '__main__':
    unittest.main()
