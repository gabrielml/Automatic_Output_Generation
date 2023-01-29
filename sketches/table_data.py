#!/usr/bin/env python3

# Convert a List of Objects into a List of Lists
# to be able to generate a table in PDF format.

# Libraries
import json

# Variables
car = {
        "id":1,
        "car": {
                "car_make":"Ford",
                "car_model":"Club Wagon",
                "car_year":1997
        },
        "price":"$5179.39",
        "total_sales":446
}


def load_data(filename):
    """Loads the contens of filename as JSON file"""
    with open(filename) as json_file:
        data = json.load(json_file)

    return data


def format_car(car):
	"""Given a car dictionary, returns a nicely formatted name."""
	return "{} {} ({})".format(
    car["car_make"], car["car_model"], car["car_year"])


def only_values(item):
	"""4.1. Returns the values of the object in a list"""
	item["car"] = format_car(item["car"])
    # (!) Convert "dict_values" to list of values!
	item_values = list(item.values())

	return item_values


def format_data(table_header, raw_data):
    """4. Returns a List of lists containing all the info to build the table of cars"""
    table = []
    # (!) Convert "map object" to list of list
    table_rows = list(map(only_values, raw_data))
    table.extend([table_header, table_rows])

    return table


def main():
    data = load_data("car_sales.json")

    table_header = ['ID', 'Car', 'Price', 'Total Sales']
    table_data = format_data(table_header, data)

    print(table_data)


if __name__ == "__main__":
    main()