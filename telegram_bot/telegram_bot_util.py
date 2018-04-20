def beer_list_in_text(beers):
    text = ""
    for i, beer in enumerate(beers):
        text += "{}. {} ({}) - {}% ABV\n".format(i+1, beer["name"], beer["style"], beer["abv"])
    return text