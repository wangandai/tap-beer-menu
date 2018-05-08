import logging
import menu_apis.apis as apis


class MenuManager:
    menus = []

    def __init__(self):
        for bar in apis.bars.keys():
            new_menu = apis.bars[bar]()
            new_menu.save_beers_to_file()
            self.menus.append(new_menu)
        logging.debug("MenuManager: MenuManager Initialized.")

    def update_menus(self):
        for m in self.menus:
            updated_m = apis.bars[m.bar]()
            if m == updated_m:
                logging.info("Menu({}) has not changed since last checked.".format(m.bar))
                continue
            m = updated_m
            m.save_beers_to_file()
        logging.info("Menus refreshed.")

    def find_good_bars(self):
        worth_going_menus = {}
        for m in self.menus:
            good_beers = m.notify_good_beers()
            if good_beers is not None:
                worth_going_menus[m.bar] = good_beers
        return worth_going_menus
