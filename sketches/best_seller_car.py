#!/usr/bin/env python3

# 1. Calculate the car model which had the most sales

# Libraries
import json
import locale
import sys

def load_data(filename):
	"""Loads the contents of filename as a JSON file"""
	with open(filename) as json_file:
		data = json.load(json_file)

	return data




def best_seller_car(data):
	"""1. Calculate the car model which had the most sales"""
	sorted_sales = sorted(data, key=lambda i: i["total_sales"], reverse=True)
	best_seller = sorted_sales[0]

	return best_seller

def main():
	data = load_data("car_sales.json")
	car_of_the_year = best_seller_car(data)
	print(car_of_the_year)


if __name__ == "__main__":
	main()