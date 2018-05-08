import logging
from models.menu import Menu


class MenuReader:
    menus = {}

    # bars is a dict of bar names and its corresponding api method
    def __init__(self, bars):
        logging.info("MenuReader: Initializing MenuManager")
        for api in bars.keys():
            self.menus[api] = Menu(api)
            self.menus[api].load_beers_from_file()

    def refresh_menu(self, menu_name):
        logging.info("MenuReader: Refreshing menu({})".format(menu_name))
        if self.menus.get(menu_name) is not None:
            self.menus[menu_name].load_beers_from_file()

    def refresh_all_menus(self):
        logging.info("MenuReader: Refreshing all menus")
        for m in self.menus.keys():
            self.menus[m].load_beers_from_file()

    def menu_list(self):
        return self.menus.keys()

    def get_menu_of(self, bar):
        return self.menus[bar]
