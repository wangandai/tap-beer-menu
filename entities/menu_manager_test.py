import unittest
from models.beer import Beer
from models.menu_section import MenuSection
from models.menu import Menu
from entities.menu_manager import MenuManager


class TestMenuManager(unittest.TestCase):

    class MockAPIPlan:
        counter = 0
        methodToCall = None
        argumentsToCall = None

        def __init__(self, method, arguments):
            self.methodToCall = method
            self.argumentsToCall = arguments

        def execute(self):
            a = self.argumentsToCall[self.counter]
            self.counter += 1
            if self.counter >= len(self.argumentsToCall):
                self.counter = 0
            return self.methodToCall(a)

        def executor(self):
            return self.execute

    def mockAPI(self, beername=""):
        return Menu("TestBar", [MenuSection("1", "Title1", [Beer("name " + beername, "style", 8, "brewery")])])

    def test_init_menus(self):
        api_dict = {
            "TestBar": self.MockAPIPlan(self.mockAPI, ["shit", "shit", "Stone", "Stone", "Founders"]).executor(),
        }
        good_menu1 = Menu("TestBar", [MenuSection("1", "Title1", [Beer("name Stone", "style", 8, "brewery")])])
        good_menu2 = Menu("TestBar", [MenuSection("1", "Title1", [Beer("name Founders", "style", 8, "brewery")])])

        mm = MenuManager(api_dict=api_dict)
        self.assertEqual({}, mm.find_good_bars())

        mm.update_menus()
        self.assertEqual({}, mm.find_good_bars())

        mm.update_menus()
        self.assertEqual({"TestBar": good_menu1}, mm.find_good_bars())

        mm.update_menus()
        self.assertEqual({}, mm.find_good_bars())

        mm.update_menus()
        self.assertEqual({"TestBar": good_menu2}, mm.find_good_bars())