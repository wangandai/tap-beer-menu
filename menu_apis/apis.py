import menu_apis.tap_api


def dummy_function():
    return []


bars = {
    "TAP Craft Beer": menu_apis.tap_api.request_menu,
    "Smith Street Taps": dummy_function,
    "Good Beer Company": dummy_function,
    "Freehouse": dummy_function,
    "American Taproom": dummy_function,
}

