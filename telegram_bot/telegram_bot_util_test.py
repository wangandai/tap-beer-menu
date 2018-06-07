import unittest
from models.menu import Menu
from models.menu_section import MenuSection
from models.beer import Beer
import telegram_bot.telegram_bot_util as util


class TestTelegramBotUtil(unittest.TestCase):

    beer_1 = Beer("Breakfast Stout", "Stout", "8.6", "Founders")
    beer_2 = Beer("Stone IPA", "IPA", "5.6", "Stone")
    section_1 = MenuSection("111", "On Tap (2 bier)", [beer_1, beer_2])
    empty_section = MenuSection("222", "Empty", [])
    menu_1 = Menu("TAP", [section_1, empty_section])

    beer_1_text = "Breakfast Stout\n" \
                    "8.6% ABV\n" \
                    "Stout\n" \
                    "Founders\n"
    beer_2_text = "Stone IPA\n" \
                  "5.6% ABV\n" \
                  "IPA\n" \
                  "Stone\n"
    section_1_text = "_On Tap_ (2 Beers)\n" \
                    "---Beer 1---\n" \
                    "{}" \
                    "---Beer 2---\n" \
                    "{}".format(beer_1_text, beer_2_text)
    menu_1_text = "*TAP*\n" \
                  "{}".format(section_1_text)

    def test_beer_in_markdown(self):
        actual_text = util.beer_to_markdown(self.beer_1)
        self.assertEqual(actual_text, self.beer_1_text)

    def test_menusection_in_markdown(self):
        actual_text = util.section_to_markdown(self.section_1)
        self.assertEqual(actual_text, self.section_1_text)

    def test_menu_in_markdown(self):
        actual_text = util.menu_to_markdown(self.menu_1)
        self.assertEqual(actual_text, self.menu_1_text)