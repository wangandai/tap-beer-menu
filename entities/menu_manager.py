import logging


class MenuManager:
    menus = {}
    notified = {}
    apis = {}

    def __init__(self, api_dict):
        self.init_menus(api_dict)
        self.apis = api_dict
        logging.debug("MenuManager: MenuManager Initialized.")

    def init_menus(self, api_dict):
        for bar in api_dict:
            new_menu = api_dict[bar]()
            new_menu.save_beers_to_file()
            self.menus[bar] = new_menu
            self.notified[bar] = False

    def update_menus(self):
        for m in self.menus:
            updated_m = self.apis[m]()
            if self.menus[m] == updated_m:
                logging.info("Menu({}) has not changed since last checked.".format(m))
                continue
            else:
                self.menus[m] = updated_m
                self.menus[m].save_beers_to_file()
                self.notified[m] = False
        logging.info("Menus refreshed.")

    def find_good_bars(self):
        should_notify = False
        worth_going_menus = {}
        for m in self.menus:
            good_menu = self.menus[m].find_good_beers()
            if good_menu is not None:
                worth_going_menus[m] = good_menu
                if self.notified[m] is not True:
                    self.notified[m] = True
                    should_notify = True
        if should_notify:
            return worth_going_menus
        return {}
