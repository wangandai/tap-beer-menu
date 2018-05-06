from menu_apis.untappd import Untappd


bars = {
    "TAP Craft Beer": Untappd("TAP Craft Beer", "https://untappd.com/v/tap-craft-beer-bar/2887707").get_menu,
    "Smith Street Taps": Untappd("Smith Street Taps", "https://untappd.com/v/smith-street-taps/1300516").get_menu,
    "Good Beer Company": Untappd("Good Beer Company", "https://untappd.com/v/the-good-beer-company/6604640").get_menu,
    "Freehouse": Untappd("Freehouse", "https://untappd.com/v/the-good-beer-company/6604640").get_menu,
    "American Taproom": Untappd("American Taproom", "https://untappd.com/v/american-taproom/7480946").get_menu,
}

