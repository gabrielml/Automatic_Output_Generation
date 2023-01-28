#!/usr/bin/env python3

# 2. Calculate the most popular car_year across all car make/models

# Libraries
import collections
import functools
import operator
import json
import locale
import sys

def load_data(filename):
  """Loads the contents of filename as JSON file"""
  with open(filename) as json_file:
    data = json.load(json_file)

    return data

def best_year(raw_data):
  """Calculate the best sales year for all car models together"""
  # Sales by year for every single car.
  # E.g. <Acura>{'2004': 100}, <Honda>{'2004': 50}
  filtered_data = list(map(selected_values, raw_data))

  # Total sales by year
  # E.g. <Acura + Honda> {'2004': 150}
  sales_by_year = dict(functools.reduce(operator.add, map(collections.Counter, filtered_data)))

  # Years sorted by sales in descending order
  desc_sales = dict(sorted(sales_by_year.items(), key=operator.itemgetter(1), reverse=True))

  # Recover the Year with the best car sales
  best_sales_year = list(desc_sales.items())[0] # Complexity would be O(n)[O(ok)]

  return best_sales_year


def selected_values(item):
  key = str(item["car"]["car_year"])
  value = item["total_sales"]
  new_item = { key : value }

  return new_item


def main():
    data = load_data("car_sales.json")
    year = best_year(data)
    print(year)

if __name__ == "__main__":
   main()