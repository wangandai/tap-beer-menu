import config.config as cfg


class Beer:
    name = ""
    style = ""
    abv = 0
    brewery = ""

    def __init__(self, name="", style="", abv=0, brewery=""):
        self.name = name
        self.style = style
        self.abv = abv
        self.brewery = brewery

    def is_worth_it(self):
        return self.is_good_brand() and self.is_abv_high_enough()

    def is_good_brand(self):
        for word in [*self.name.split(), self.brewery]:
            if str.lower(word) in cfg.good_brands:
                return True
        return False

    def is_abv_high_enough(self):
        return self.abv >= cfg.cutoff_abv

    def to_text(self):
        return "{} [{}] - {}% ABV".format(self.name, self.style, self.abv)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.name == other.name and self.style == other.style and self.abv == other.abv and self.brewery == other.brewery
        return False

    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return self.name != other.name or self.style != other.style or self.abv != other.abv or self.brewery != other.brewery

    def __repr__(self):
        return "Beer(name={0.name}, style={0.style}, abv={0.abv}, brewery={0.brewery})".format(self)

    def to_dict(self):
        return {
            "name": self.name,
            "style": self.style,
            "abv": self.abv,
            "brewery": self.brewery
        }

    def from_dict(self, d):
        self.name = d["name"]
        self.style = d["style"]
        self.abv = d["abv"]
        self.brewery = d["brewery"]
        return self
