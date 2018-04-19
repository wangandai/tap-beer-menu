import requests
import re
import html


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
