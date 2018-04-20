import logging
import config.config as cfg
import menu_apis.tap_api
import entities.menu as menu


class MenuManager:
    menus = []
    bars = {
        "tap": menu_apis.tap_api.request_menu,
    }

    def __init__(self):
        for bar in self.bars.keys():
            new_menu = menu.Menu(bar)
            new_menu.update_beers(self.bars[bar]())
            new_menu.save_beers_to_file()
            self.menus.append(new_menu)
        logging.debug("MenuManager: MenuManager Initialized")

    def update_menus(self):
        for m in self.menus:
            m.update_beers(self.bars[m.name]())
            m.save_beers_to_file()

    def find_good_bars(self):
        worth_going_menus = []
        for m in self.menus:
            logging.info(m.was_updated)
            if m.is_worth_going() and m.was_updated:
                worth_going_menus.append(m)
        return worth_going_menus
