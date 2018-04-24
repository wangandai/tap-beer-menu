import logging
import config.config as cfg
from models.menu import Menu
import menu_apis.apis as apis


class MenuReader:
    menus = {}

    def __init__(self):
        logging.info("MenuReader: Initializing MenuManager")
        for api in apis.bars.keys():
            self.menus[api] = Menu(api)
            self.menus[api].load_beers_from_file()

    def refresh_menu(self, menu_name):
        logging.info("MenuReader: Updating menus")
        if self.menus.get(menu_name) is not None:
            self.menus[menu_name].load_beers_from_file()

    def menu_list(self):
        return self.menus.keys()

    def get_menu_of(self, bar):
        return self.menus[bar]
