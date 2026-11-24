# DevTrack risk analysis test

def calculate_total(values):
    total = 0

    for value in values:
        total += value

    return total


def calculate_average(values):
    if not values:
        return 0

    return calculate_total(values) / len(values)


def find_maximum(values):
    if not values:
        return None

    maximum = values[0]

    for value in values:
        if value > maximum:
            maximum = value

    return maximum
