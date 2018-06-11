import logging
from models.menu import Menu


class MenuReader:
    menus = {}

    # bars is a dict of bar names and its corresponding api method
    def __init__(self, bars):
        for api in bars.keys():
            self.menus[api] = Menu(api)
            self.menus[api].load_beers_from_file()
        logging.info("MenuReader Initialized")

    def refresh_menu(self, menu_name):
        if self.menus.get(menu_name) is not None:
            self.menus[menu_name].load_beers_from_file()
            logging.info("MenuReader: Refreshed menu({})".format(menu_name))
        else:
            logging.warning("MenuReader: No menu found for {}".format(menu_name))

    def refresh_all_menus(self):
        for m in self.menus.keys():
            self.menus[m].load_beers_from_file()
        logging.info("MenuReader: All menus refreshed.")

    def menu_list(self):
        return self.menus.keys()

    def get_menu_of(self, bar):
        return self.menus[bar]

    def find_good_bars(self):
        worth_going_menus = {}
        for m in self.menus:
            good_menu = self.menus[m].find_good_beers()
            if good_menu is not None:
                worth_going_menus[m] = good_menu
        return worth_going_menus
