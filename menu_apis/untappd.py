from lxml import html
import re
import logging
import requests
import json
from models.beer import Beer
from models.menu_section import MenuSection
from models.menu import Menu


class Untappd:
    url = ""
    bar_id = ""
    bar_name = ""
    cookies = None

    basic_headers = {
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'authority': 'untappd.com',
     }

    def __init__(self, bar_name, url):
        url_check = re.search("https:\/\/untappd.com\/v\/.+?\/([0-9]+)$", url)
        if url_check is not None:
            self.url = url
            self.bar_id = url_check.group(1)
            self.bar_name = bar_name
        else:
            logging.error("Error creating Untappd API for: {}".format(url))
            raise ValueError

    def get_page(self):
        h1 = {
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'cache-control': 'max-age=0',
        }
        h1.update(self.basic_headers)

        r1 = requests.get(self.url, headers=h1)
        self.cookies = r1.cookies
        return r1.content.decode('utf-8')

    def request_for_section(self, section_id):
        h2 = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'referer': self.url,
            'x-requested-with': 'XMLHttpRequest',
        }
        h2.update(self.basic_headers)

        params = (
            ('section_id', section_id),
        )

        r2 = requests.get('https://untappd.com/venue/more_menu/{}/15'.format(self.bar_id),
                          headers=h2,
                          params=params,
                          cookies=self.cookies)
        return r2.content.decode('utf-8')

    def load_section(self, section_id):
        loaded_content = self.request_for_section(section_id)
        loaded_html = json.loads(loaded_content)["view"]
        return html.fragments_fromstring(loaded_html)

    @staticmethod
    def get_abv_from_span(text):

        try:
            matches = re.search("(.+?)% ABV.*", text)
            return float(matches.group(1))
        except (ValueError, AttributeError):
            logging.error("Could not parse ABV from text: {}".format(text))
            return 0

    def build_menu_from_html(self, page):
        tree = html.document_fromstring(page)
        m = Menu(self.bar_name)

        # Get all menu sections
        sections = tree.find_class("menu-section")

        for section in sections:
            # Get section details
            section_id_string = section.get("id")
            section_id = re.search("section_(.+?)$", section_id_string).group(1)
            title = section.find_class("menu-section-header")[0].text_content()
            beer_list = section.find_class("menu-section-list")
            beers = beer_list[0].getchildren()
            # If not all beers are loaded
            if len(section.find_class("show-more-section")) > 0:
                logging.debug("Loading more beers for {}.".format(section_id_string))
                beers += self.load_section(section_id)

            # There are beers in this section
            if len(beers) > 0:
                ms = MenuSection(section_id, title)
                for beer in beers:
                    details = beer.find_class("beer-details")[0]
                    h5, h6 = details.getchildren()
                    name, style = h5.getchildren()
                    abv = h6.getchildren()[0]
                    brewery = h6.getchildren()[0].getchildren()[0]
                    ms.beers.append(Beer(name.text_content(),
                                         style.text_content(),
                                         self.get_abv_from_span(abv.text_content()),
                                         brewery.text_content())
                                    )
                m.sections.append(ms)
        return m

    def get_menu(self):
        return self.build_menu_from_html(self.get_page())