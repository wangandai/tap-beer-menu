import re


def beer_list_in_text(beers):
    if len(beers) == 0:
        return "No beers available."
    text = ""
    for i, beer in enumerate(beers):
        text += "{}. {} ({}) - {}% ABV\n".format(i+1, beer.name, beer.type, beer.abv)
    return text


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def get_command(text):
    pattern = re.compile("\/(.+?)(?:@.*|\Z)")
    matched = pattern.match(text)
    if matched:
        return matched.group(1)
    else:
        return text
