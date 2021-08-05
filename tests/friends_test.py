import unittest
from src.friends import *


class TestFriends(unittest.TestCase):

    def setUp(self):

        self.person1 = {
            "name": "Shaggy",
            "age": 12,
            "monies": 1,
            "friends": ["Velma", "Fred", "Daphne", "Scooby"],
            "favourites": {
                "tv_show": "friends",
                "snacks": ["charcuterie"]
            }
        }

        self.person2 = {
            "name": "Velma",
            "age": 15,
            "monies": 2,
            "friends": ["Fred"],
            "favourites": {
                "tv_show": "Baywatch",
                "snacks": ["soup", "bread"]
            }
        }

        self.person3 = {
            "name": "Scooby",
            "age": 18,
            "monies": 20,
            "friends": ["Shaggy", "Velma"],
            "favourites": {
                "tv_show": "Pokemon",
                "snacks": ["Scooby snacks"]
            }
        }

        self.person4 = {
            "name": "Fred",
            "age": 18,
            "monies": 20,
            "friends": ["Shaggy", "Velma", "Daphne"],
            "favourites": {
                "tv_show": "X-Files",
                "snacks": ["spaghetti", "ratatouille"]
            }
        }

        self.person5 = {
            "name": "Daphne",
            "age": 20,
            "monies": 100,
            "friends": [],
            "favourites": {
                "tv_show": "X-Files",
                "snacks": ["spinach"]
            }
        }

        self.people = [self.person1, self.person2,
                       self.person3, self.person4, self.person5]

    # 1. For a given person, return their name
    def test_getting_name(self):
        result = get_name(self.person5)
        self.assertEqual("Daphne", result)

    # 2. For a given person, return their favourite tv show
    # (e.g. the function favourite_tv_show(self.person2) should return the string "Baywatch")
    def test_get_favourite_tv_show(self):
        result = get_favourite_tv_show(self.person2)
        self.assertEqual("Baywatch", result)

    # 3. For a given person, check if they like a particular food
    # (e.g. the function likes_to_eat(self.person2, "bread") should return True, likes_to_eat(self.person3, "spinach") should return False)

    def test_person_likes_food__True(self):
        self.assertEqual(True, likes_to_eat(self.person2, "bread"))

    def test_person_likes_food__False(self):
        self.assertEqual(False, likes_to_eat(self.person3, "spinach"))

    # 4. For a given person, add a new name to their list of friends
    # (e.g. the function add_friend(self.person2, "Scrappy-Doo") should add Scrappy-Doo to the friends.)
    # (hint: This function should not return anything. After the function call, check for the length of the friends array to test it!)

    def test_add_friend(self):
        add_friend(self.person2, "Scrappy-Doo")
        self.assertEqual(2, len(self.person2["friends"]))

    # 5. For a given person, remove a specific name from their list of friends
    # (hint: Same as above, testing for the length of the array should be sufficient)

    def test_remove_friend(self):
        add_friend(self.person2, "Scrappy-Doo")
        remove_friend(self.person2, "Fred")
        self.assertEqual(1, len(self.person2["friends"]))

    # 6. Find the total of everyone's money
    # (hint: use the self.people array, remember how we checked the total number of eggs yesterday?)

    def test_total_money(self):
        self.assertEqual(143, total_money(self.people))

    # 7. For two given people, allow the first person to loan a given value of money to the other
    # (hint: our function will probably need 3 arguments passed to it... the lender, the lendee, and the amount for this function)

    def test_lend_money(self):
        lend_money(self.person2, self.person1, 2)
        self.assertEqual(0, self.person2["monies"])
        self.assertEqual(3, self.person1["monies"])

    # 8. Find the set of everyone's favourite food joined together
    # (hint: concatenate the favourites/snack arrays together)

    def test_favourite_foods(self):
        result = all_favourite_foods(self.people)
        expected = ["charcuterie", "soup", "bread",
                    "Scooby snacks", "spaghetti", "ratatouille", "spinach"]
        self.assertEqual(expected, result)

    # 9. Find people with no friends
    # (hint: return a list, there might be more people in the future with no friends!)

    def test_find_no_friends(self):
        self.assertEqual([self.person5], find_no_friends(self.people))

    # 10. Given two people, find out which friends they have in common
    # (hint: use the in keyword to check if each of the friends appears in the other person's list of friends)

    def test_find_mutual_friends(self):
        self.assertEqual(["Velma", "Daphne"], find_mutual_friends(
            self.person1, self.person4))

    # 11. Find all of the people who enjoy a particular TV show
    # (hint: return a list. We don't know how many people we will need to return)

    def test_find_people_who_like_tv_show(self):
        self.assertEqual([self.person4, self.person5],
            find_people_who_like_tv_show("X-Files", self.people))

    # 12. Find the oldest person
    # (hint: Use a loop to compare each person's age to the highest age that you have seen so far)

    def test_find_oldest_person(self):
        self.assertEqual(self.person5, find_oldest_person(self.people))

    # 13. Create a list of everyone's favourite TV shows without duplicates

    @unittest.skip("delete this line to run the test")
    def test_all_favourite_tv_shows(self):
        expected = ["friends", "Baywatch", "Pokemon", "X-Files"]
        self.assertEqual(expected, all_favourite_tv_shows(self.people))
