import unittest
from entities.menu_reader import MenuReader
from models.menu import Menu


class TestMenuReader(unittest.TestCase):

    def test_Constructor(self):
        bars = {
            "TestBar": 0,
        }
        mr = MenuReader(bars)
        self.assertEqual(1, len(mr.menus.keys()))

    def test_GetMenu(self):
        bars = {
            "TestBar": 0,
        }
        mr = MenuReader(bars)
        expected = Menu("TestBar")
        expected.load_beers_from_file()
        self.assertEqual(expected, mr.get_menu_of("TestBar"))


if __name__ == "__main__":
    unittest.main()