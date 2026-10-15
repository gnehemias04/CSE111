"""
Author: Gabriel Nehemias Rengifo Krunfli
Name: Boss Stock Check
Description: A simple Python tool to manage store inventory.
"""

import csv
import datetime


def read_products(filename, key_column_index ):
    products={}
    """Open and read the products file"""
    with open(filename, "rt") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader :
            key_value = row[key_column_index]
            products[key_value]=row
    return products


def display_products(filename):
    KEY_INDEX=0
    NAME_INDEX=1
    STOCK_INDEX=2
    PRICE_INDEX=3
    products = read_products(filename, KEY_INDEX)
    display = ""
    for product in products:
        row = products[product]
        key = row[KEY_INDEX]
        name = row[NAME_INDEX]
        stock = row[STOCK_INDEX]
        price = row[PRICE_INDEX]
        display += "Item:" + key  + "  | Stock:" + stock + "  | Price: $" + price + " | Name:" + name + "\n"
    print(display)
    return display


def add_product():
    pass


def update_product():
    pass


def find_product():
    pass


def save_products():
    pass

def date_time():
    time = datetime.datetime.now()
    today = time.ctime()
    print(today)
    return today


def main():
    print("========================================\n            BOSS STOCK CHECK \n========================================")
    date_time()
    print("")
    display_products("products.csv")
    print("Hello! What do you want to do?")
    print("1. Update a product")
    print("2. Add a product")
    print("3. Exit")
    option = int(input("Choose an option: "))
    
    

    
if __name__ == "__main__":
    main()


