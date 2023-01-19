SIZES = [
    {
        "id": 1,
        "carets": 24,
        "price": 2500.50
    },
    {
        "id": 2,
        "carets": 48,
        "price": 5200.75
    },
    {
        "id": 3,
        "carets": 72,
        "price": 6700.75
    }
]


def get_all_sizes():
    return SIZES


def get_single_size(id):
    # Variable to hold the found animal, if it exists
    requested_size = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size
