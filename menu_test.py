import unittest
import menu

class TestMenuMethods(unittest.TestCase):

    def test_isABVHighEnough(self):
        high_abv = 8.5
        equal_abv = 8.0
        low_abv = 5.0

        self.assertTrue(menu.is_abv_high_enough(high_abv))
        self.assertTrue(menu.is_abv_high_enough(equal_abv))
        self.assertFalse(menu.is_abv_high_enough(low_abv))

    def test_isGoodbrand(self):
        good_brands = ["Deschutes Mirror Pond", "Breakfast Stout Founders", "STONE IPA"]
        bad_brands = ["lousy brand beer", "tiger beer"]
        for brand in good_brands:
            self.assertTrue(menu.is_good_brand(brand))
        for brand in bad_brands:
            self.assertFalse(menu.is_good_brand(brand))

    def test_isworthgoing(self):
        worth_going = [
            {
                "name": "Founders Breakfast Stout",
                "abv": 8.5,
            },
            {
                "name": "So so beer",
                "abv": 4.0,
            }
        ]
        not_worth_going_bad_beers = [
            {
                "name": "Tiger beer",
                "abv": 8.0,
            },
            {
                "name": "Chang beer",
                "abv": 8.0,
            }
        ]
        not_worth_going_low_abv = [
            {
                "name": "Founders Breakfast",
                "abv": 5.0,
            },
            {
                "name": "Poor IPA",
                "abv": 8.0,
            }
        ]
        worth, _ = menu.is_worth_going(worth_going)
        self.assertTrue(worth)

        worth, _ = menu.is_worth_going(not_worth_going_low_abv)
        self.assertFalse(worth)

        worth, _ = menu.is_worth_going(not_worth_going_bad_beers)
        self.assertFalse(worth)


if __name__ == '__main__':
    unittest.main()