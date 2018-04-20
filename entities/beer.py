import config.config as cfg


class Beer:
    name = ""
    type = ""
    abv = 0

    def __init__(self, name, type, abv):
        self.name = name
        self.type = type
        self.abv = abv

    def is_worth_it(self):
        return self.is_good_brand() and self.is_abv_high_enough()

    def is_good_brand(self):
        for word in self.name.split():
            if str.lower(word) in cfg.good_brands:
                return True
        return False

    def is_abv_high_enough(self):
        return self.abv > cfg.cutoff_abv

    def to_string(self):
        return "{} [{}] - {}% ABV".format(self.name, self.type, self.abv)
