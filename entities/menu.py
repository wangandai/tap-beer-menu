import requests
import re
import html


# Retrieves the menu for today
def get_today_menu():
    # Get menu location
    headers = {
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

    response1 = requests.get('http://menu.tapthat.com.sg/', headers=headers)
    # print(response1.content)

    response_string = response1.content.decode('utf-8')

    groups = re.search('PreloadEmbedMenu\("menu-container",([0-9]+),([0-9]+)\)', response_string)
    # print(groups[1], groups[2])

    # Retrieve menu
    response2 = requests.get('https://business.untappd.com/locations/{}/themes/{}/js'.format(groups[1], groups[2]), headers=headers)

    # print(response.content)

    menu_html = str(response2.content)
    menu_html = ' '.join(menu_html.replace('\\n', '').replace('\\', '').split())
    menu_html = html.unescape(menu_html)
    # print(menu_html)

    beer_regex = re.compile('<!-- Beer Name \+ Style -->.+?<\/span>(.+?)\s<\/a>.+?item-title-color">(.+?)<\/span>.+?"abv">(.+?)%\sABV', re.DOTALL)
    beer_groups = beer_regex.finditer(menu_html)

    beers = []
    for beer_group in beer_groups:
        beers.append(
            {
                'name': beer_group[1],
                'style': beer_group[2],
                'abv': float(beer_group[3]),
            }
        )

    return beers


# Returns: is_worth_going(bool), beers(dict)
def is_worth_going(menu):
    good_beers = []
    for beer in menu:
        if is_good_brand(beer["name"]) and is_abv_high_enough(beer["abv"]):
            good_beers.append(beer)

    return len(good_beers) > 0, good_beers


def is_good_brand(name):
    good_beers_list = ["deschutes", "founders", "brewlander", "stone", "cloudwater", "rouge", "heretic", "omnipollo"]
    for brand in good_beers_list:
        if brand in str.lower(name).split(" "):
            return True
    return False


def is_abv_high_enough(abv):
    return abv >= 8.0
