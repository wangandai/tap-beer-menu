import unittest
from models.menu_section import MenuSection
from models.beer import Beer


class TestMenuSection(unittest.TestCase):

    def test_Constructor(self):
        section_1 = MenuSection("123", "Beers")
        section_2 = MenuSection("124", "More beers", [Beer("B", "EE", 1.0, "R")])
        self.assertEqual(section_1.section_id, "123")
        self.assertEqual(section_1.title, "Beers")
        self.assertEqual(len(section_1.beers), 0)
        self.assertEqual(section_2.section_id, "124")
        self.assertEqual(section_2.title, "More beers")
        self.assertEqual(len(section_2.beers), 1)
        self.assertEqual(section_2.beers[0], Beer("B", "EE", 1.0, "R"))

    def test_MenuSectionEquals(self):
        section_1 = MenuSection("123", "Beers")
        section_2 = MenuSection("123", "Beers")
        for i in range(3):
            section_1.beers.append(Beer(str(i), str(i), i, str(i)))
            section_2.beers.append(Beer(str(i), str(i), i, str(i)))
        self.assertEqual(section_1, section_2, "Should be equal")

    def test_MenuSectionUnequals(self):
        section_1 = MenuSection("123", "Beers")
        section_2 = MenuSection("124", "Beers")
        section_3 = MenuSection("123", "beers")
        section_4 = MenuSection("124", "beers")
        for i in range(3):
            section_1.beers.append(Beer(str(i), str(i), i, str(i)))
            section_2.beers.append(Beer(str(i), str(i), i, str(i)))
            section_3.beers.append(Beer(str(i), str(i), i, str(i)))
        section_1.beers.append(Beer("different", "section", 5.0, "brew"))
        self.assertNotEqual(section_1, section_2, "Should not be equal")
        self.assertNotEqual(section_1, section_3, "Should not be equal")
        self.assertNotEqual(section_1, section_4, "Should not be equal")

    def test_ToDict(self):
        section = MenuSection("123", "Beers")
        section.beers.append(Beer("One beer", "From", 18.0, "There"))
        section.beers.append(Beer("Two beer", "From", 9.0, "Here"))
        section_dict = {
            "section_id": "123",
            "title": "Beers",
            "beers": [{
                "name": "One beer",
                "style": "From",
                "abv": 18.0,
                "brewery": "There"
            }, {
                "name": "Two beer",
                "style": "From",
                "abv": 9.0,
                "brewery": "Here"
            }]
        }
        self.assertEqual(section.to_dict(), section_dict)

    def test_FromDict(self):
        section = MenuSection("123", "Beers")
        section.beers.append(Beer("One beer", "From", 18.0, "There"))
        section.beers.append(Beer("Two beer", "From", 9.0, "Here"))
        section_dict = {
            "section_id": "123",
            "title": "Beers",
            "beers": [{
                "name": "One beer",
                "style": "From",
                "abv": 18.0,
                "brewery": "There"
            }, {
                "name": "Two beer",
                "style": "From",
                "abv": 9.0,
                "brewery": "Here"
            }]
        }
        self.assertEqual(section, MenuSection().from_dict(section_dict))

    def test_GoodBeers(self):
        section = MenuSection("123", "Beers")
        section.beers.append(Beer("One beer", "From", 18.0, "There"))
        section.beers.append(Beer("Breakfast Stout", "From", 9.0, "Founders"))
        good_beers = section.good_beers()
        self.assertEqual(len(good_beers), 1)
        self.assertEqual(good_beers[0], Beer("Breakfast Stout", "From", 9.0, "Founders"))


if __name__ == "__main__":
    unittest.main()