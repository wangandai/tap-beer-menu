import unittest
from models.beer import Beer


class TestBeer(unittest.TestCase):

    def test_BeerEquals(self):
        b1 = Beer("Breakfast stout", "Stout", 8.0, "Founders")
        b2 = Beer("Breakfast stout", "Stout", 8.0, "Founders")
        self.assertEqual(b1, b2)

    def test_BeerUnEquals(self):
        b1 = Beer("Breakfast stout", "Stout", 8.0, "Founders")
        b2 = Beer("Breakfast Stout", "Stout", 8.0, "Founders")
        b3 = Beer("Breakfast stout", "IPA", 8.0, "Founders")
        b4 = Beer("Breakfast stout", "Stout", 7.0, "Founders")
        b5 = Beer("Breakfast stout", "Stout", 8.0, "Stone")
        self.assertNotEqual(b1, b2)
        self.assertNotEqual(b1, b3)
        self.assertNotEqual(b1, b4)
        self.assertNotEqual(b1, b5)

    def test_IsWorthIt(self):
        b1 = Beer("Breakfast stout", "Stout", 8.0, "Founders")
        b2 = Beer("Founders Breakfast stout", "Stout", 8.0, "None")
        self.assertEqual(b1.is_worth_it(), True)
        self.assertEqual(b2.is_worth_it(), True)

    def test_IsNotWorthIt(self):
        b1 = Beer("Breakfast stout", "Stout", 5.0, "No Brand")
        b2 = Beer("Breakfast stout", "Stout", 8.0, "Some Brand")
        b3 = Beer("Breakfast stout", "Stout", 6.0, "Founders")
        self.assertEqual(b1.is_worth_it(), False)
        self.assertEqual(b2.is_worth_it(), False)
        self.assertEqual(b3.is_worth_it(), False)

    def test_repr(self):
        b = Beer("Breakfast stout", "Stout", 8.0, "Founders")
        self.assertEqual(str(b), "Beer(name=Breakfast stout, style=Stout, abv=8.0, brewery=Founders)")

    def test_ToDict(self):
        b = Beer("Breakfast stout", "Stout", 8.0, "Founders")
        b_dict = {
            "name": "Breakfast stout",
            "style": "Stout",
            "abv": 8.0,
            "brewery": "Founders"
        }
        self.assertEqual(b.to_dict(), b_dict)

    def test_FromDict(self):
        b = Beer("Breakfast stout", "Stout", 8.0, "Founders")
        b_dict = {
            "name": "Breakfast stout",
            "style": "Stout",
            "abv": 8.0,
            "brewery": "Founders"
        }
        self.assertEqual(b, Beer().from_dict(b_dict))


if __name__ == "__main__":
    unittest.main()