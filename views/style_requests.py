STYLES = [
    {
        "id": 1,
        "style": "Ugly",
        "price": 9500.50
    },
    {
        "id": 2,
        "style": "Pretty",
        "price": 125.50
    },
    {
        "id": 3,
        "style": "Cool",
        "price": 150.50
    },
]


def get_all_styles():
    return STYLES


def get_single_style(id):
    # Variable to hold the found animal, if it exists
    requested_style = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for style in STYLES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style
