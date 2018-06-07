import re


def beer_list_in_text(beers):
    if len(beers) == 0:
        return "No beers available."
    text = ""
    for beer in beers:
        text += "---\n" \
                "{}\n" \
                "{}% ABV\n" \
                "{}\n" \
                "{}\n".format(beer.name, beer.abv, beer.style, beer.brewery)
    return text


def good_beers_in_text(bar_name, sections):
    message = ""
    message += "*At {} bar:*\n".format(bar_name)
    for section in sections:
        title = trim_section_title(section["section"])
        message += "_{}_\n{}\n\n".format(title, beer_list_in_text(section["good_beers"]))
    return message


def section_in_text(section_title, beer_list):
    message = ""
    title = trim_section_title(section_title)
    message += "_{}_\n{}\n".format(title, beer_list_in_text(beer_list))
    return message


def display_whole_menu(menu):
    message = "*{}*\n".format(menu.bar)
    for section in menu.sections:
        message += section_in_text(section.title, section.beers)
    return message


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


def trim_section_title(title):
    return title.split("(")[0].strip()


def beer_to_markdown(beer_obj):
    text = "{}\n" \
           "{}% ABV\n" \
           "{}\n" \
           "{}\n".format(beer_obj.name, beer_obj.abv, beer_obj.style, beer_obj.brewery)
    return text


def section_to_markdown(section_obj):
    if len(section_obj.beers) == 0:
        return ""

    plural = "s" if len(section_obj.beers) > 0 else ""
    text = "_{}_ ({} Beer{})\n".format(trim_section_title(section_obj.title), len(section_obj.beers), plural)
    for i, beer in enumerate(section_obj.beers):
        text += "---Beer {}---\n".format(i+1)
        text += beer_to_markdown(beer)
    return text


def menu_to_markdown(menu_obj):
    text = "*{}*\n".format(menu_obj.bar)
    for section in menu_obj.sections:
        text += section_to_markdown(section)
    return text
