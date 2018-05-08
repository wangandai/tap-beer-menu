import unittest
from models.menu import Menu
from models.beer import Beer
from models.menu_section import MenuSection
import os


class TestMenu(unittest.TestCase):

    def test_Constructor(self):
        menu_1 = Menu("Bar")
        menu_2 = Menu("Bar2", [MenuSection()])
        self.assertEqual(menu_1.bar, "Bar")
        self.assertEqual(len(menu_1.sections), 0)
        self.assertEqual(menu_2.bar, "Bar2")
        self.assertEqual(len(menu_2.sections), 1)

    def test_ToDict(self):
        section = MenuSection("123", "Beers")
        section.beers.append(Beer("One beer", "From", 18.0, "There"))
        section.beers.append(Beer("Two beer", "From", 9.0, "Here"))
        menu = Menu("Bar", [section])
        menu_dict = {
            "bar": "Bar",
            "sections": [{
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
            }],
        }
        self.assertEqual(menu.to_dict(), menu_dict)

    def test_FromDict(self):
        section = MenuSection("123", "Beers")
        section.beers.append(Beer("One beer", "From", 18.0, "There"))
        section.beers.append(Beer("Two beer", "From", 9.0, "Here"))
        menu = Menu("Bar", [section])
        menu_dict = {
            "bar": "Bar",
            "sections": [{
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
            }],
        }
        self.assertEqual(menu, Menu().from_dict(menu_dict))

    def test_MenuEqual(self):
        menu_1 = Menu("Bar1", [MenuSection("1", "Title1", [Beer("name", "style", 8.0, "brewery")])])
        menu_2 = Menu("Bar1", [MenuSection("1", "Title1", [Beer("name", "style", 8.0, "brewery")])])
        self.assertEqual(menu_1, menu_2)

    def test_MenuUnequal(self):
        menu_1 = Menu("Bar1", [MenuSection("1", "Title1", [Beer("name", "style", 8.0, "brewery")])])
        menu_2 = Menu("Bar2", [MenuSection("1", "Title1", [Beer("name", "style", 8.0, "brewery")])])
        menu_3 = Menu("Bar1", [MenuSection("2", "Title1", [Beer("name", "style", 8.0, "brewery")])])
        menu_4 = Menu("Bar1", [MenuSection("1", "Title2", [Beer("name", "style", 8.0, "brewery")])])
        menu_5 = Menu("Bar1", [MenuSection("1", "Title1", [Beer("nameaa", "style", 8.0, "brewery")])])
        menu_6 = Menu("Bar1", [MenuSection("1", "Title1", [Beer("name", "style", 8.0, "brewery"), Beer("name", "style", 8.0, "brewery")])])
        self.assertNotEqual(menu_1, menu_2)
        self.assertNotEqual(menu_1, menu_3)
        self.assertNotEqual(menu_1, menu_4)
        self.assertNotEqual(menu_1, menu_5)
        self.assertNotEqual(menu_1, menu_6)

    def test_SaveLoad(self):
        os.chdir("..")
        menu_1 = Menu("TestBar", [MenuSection("1", "Title1", [Beer("name", "style", 8.0, "brewery")])])
        menu_1.save_beers_to_file()
        self.assertEqual(os.path.isfile(menu_1.data_file()), True)
        menu_2 = Menu("TestBar")
        menu_2.load_beers_from_file()
        self.assertEqual(menu_1, menu_2)

    def test_FindGoodBeers(self):
        menu_1 = Menu("TestBar", [MenuSection("1", "Title1", [Beer("Founders", "Stout", 8.0, "Founders"),                                                    Beer("Shit", "Stout", 8.0, "Shit")])])
        gd_beers = [{
            "section": "Title1",
            "good_beers": [Beer("Founders", "Stout", 8.0, "Founders")]
        }]
        self.assertEqual(gd_beers, menu_1.find_good_beers())
        menu_2 = Menu("TestBar", [MenuSection("1", "Title1", [Beer("Crap", "Stout", 8.0, "Crap"),
                                                              Beer("Shit", "Stout", 8.0, "Shit")])])
        self.assertEqual([], menu_2.find_good_beers())

    def test_Notify(self):
        section = MenuSection("123", "Beers")
        section.beers.append(Beer("One beer", "From", 18.0, "Founders"))
        section.beers.append(Beer("Two beer", "From", 9.0, "Here"))
        menu = Menu("Bar", [section])
        self.assertIsNone(menu.get_time_notified())
        self.assertIsNotNone(menu.notify_good_beers())

        self.assertIsNotNone(menu.get_time_notified())
        self.assertIsNone(menu.notify_good_beers())
        self.assertGreater(menu.get_time_notified(), menu.get_time_updated())


if __name__ == "__main__":
    unittest.main()

