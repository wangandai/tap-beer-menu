import re


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


def multiple_menus_to_markdown(menu_dict):
    text = ""
    for menu in menu_dict:
        if text != "":
            text += "\n"
        text += menu_to_markdown(menu_dict[menu])
    return text
