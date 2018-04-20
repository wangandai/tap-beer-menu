import logging
import menu_apis.tap_api as tap
from entities.menu import Menu


class MenuReader:
    menus = {}
    menu_apis = {"tap": tap.request_menu}

    def __init__(self):
        logging.info("MenuManager: Initializing MenuManager")
        for bar in self.menu_apis.keys():
            self.menus[bar] = Menu(bar)

    def update_menu(self, menu_name):
        logging.info("MenuManager: Updating menus")
        if self.menus.get(menu_name) is not None:
            self.menus[menu_name].update_beers(self.menu_apis[menu_name]())

    def menu_list(self):
        return self.menus.keys()

    def get_menu_of(self, bar):
        return self.menus[bar]
