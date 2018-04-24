import logging
import models.menu as menu
import menu_apis.apis as apis


class MenuManager:
    menus = []

    def __init__(self):
        for bar in apis.bars.keys():
            new_menu = menu.Menu(bar)
            new_menu.update_beers(apis.bars[bar]())
            new_menu.save_beers_to_file()
            self.menus.append(new_menu)
        logging.debug("MenuManager: MenuManager Initialized.")

    def update_menus(self):
        for m in self.menus:
            m.update_beers(apis.bars[m.name]())
            m.save_beers_to_file()
        logging.info("Menus refreshed.")

    def find_good_bars(self):
        worth_going_menus = []
        for m in self.menus:
            logging.info("Menu({}) updated since last checked: {}".format(m.name, m.was_updated))
            if m.is_worth_going() and m.was_updated:
                worth_going_menus.append(m)
        return worth_going_menus
