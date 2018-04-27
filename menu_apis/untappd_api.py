import requests
import re
import logging
import lxml


def get_from_untapped(untappd_url):
    find_venue_id = re.compile("https:\/\/untappd.com\/v\/.+?\/(.+?)$")
    find_beer_list = re.compile("<ul class=\"menu-section-list\" id=\"section-menu-list-(.+?)\">(.+?)<\/ul>")
    find_beers_initial = re.compile('<li> <div class="beer-info ">.+?<div class="beer-details">.+?">(.+?)<\/a> <em>(.+?)<\/em><\/h5> <h6><span>(.+?)% ABV.+?">(.+?)<\/a>.+?<\/span><\/h6> <\/div> <\/div> <\/li>')

    h1 = {
        'accept-language': 'en-US,en;q=0.9',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'cache-control': 'max-age=0',
        'authority': 'untappd.com',
    }

    r1 = requests.get(untappd_url, headers=h1)
    print(r1.content)

    # h2 = {
    #     'accept-language': 'en-US,en;q=0.9',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    #     'accept': 'application/json, text/javascript, */*; q=0.01',
    #     'referer': untappd_url,
    #     'authority': 'untappd.com',
    #     'x-requested-with': 'XMLHttpRequest',
    # }
    #
    # params = (
    #     ('section_id', '47585901'),
    # )
    #
    # r2 = requests.get('https://untappd.com/venue/more_menu/2887707/15', headers=h2, params=params, cookies=r1.cookies)
    # print(r2.content)


get_from_untapped('https://untappd.com/v/tap-craft-beer-bar/2887707')