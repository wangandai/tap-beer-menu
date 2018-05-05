from models.beer import Beer
from models.util import are_lists_equal


class MenuSection:

    # id contains section ID from HTML (string)
    section_id = ""
    # title contains title from HTML (string)
    title = ""
    # beers contains array of Beer objects (Beer[])
    beers = None

    def __init__(self, section_id="", title="", beers=None):
        self.section_id = section_id
        self.title = title
        self.beers = beers
        if self.beers is None:
            self.beers = []

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.section_id == other.section_id and self.title == other.title and self.__beer_list_eq__(other.beers)
        return False

    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return self.section_id != other.section_id or self.title != other.title or not self.__beer_list_eq__(other.beers)

    def __beer_list_eq__(self, other_beers):
        return are_lists_equal(self.beers, other_beers)

    def __repr__(self):
        return "MenuSection(section_id={0.section_id}, title={0.title}, beers={0.beers})".format(self)

    def to_dict(self):
        return {
            "section_id": self.section_id,
            "title": self.title,
            "beers": [b.to_dict() for b in self.beers]
        }

    def from_dict(self, d):
        self.section_id = d["section_id"]
        self.title = d["title"]
        self.beers = [Beer().from_dict(b) for b in d["beers"]]
        return self

    def good_beers(self):
        return [b for b in self.beers if b.is_worth_it()]
