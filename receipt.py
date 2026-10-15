"""
Gabriel Nehemias Rengifo
W05 Project: Grocery Store

"""

import csv
import datetime as dt


def read_dictionary(filename, key_column_index):
    s_dictionary={}
    """Open and read the products file"""
    with open(filename, "rt") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader :
            key_value = row[key_column_index]
            s_dictionary[key_value]=row
    return s_dictionary

def main():
    KEY_INDEX=0
    NAME_INDEX=1
    PRICE_INDEX=2
    number_item = 0
    subtotal = 0
    receipt = ""
    time = dt.datetime.now()
    today = time.ctime()
    try:
        products_dict = read_dictionary("products.csv", KEY_INDEX)
    except FileNotFoundError as file_err:
        print(f"Error: {file_err}")
        return

    except PermissionError as perm_err:
        print(perm_err)
        return
        

    """Open and read the request file"""
    try:
        with open("request.csv", "rt") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            next(csvreader)
            for row in csvreader :
                key_value = row[KEY_INDEX]
                product = products_dict[key_value]
                number_item = number_item + int(row[NAME_INDEX])
                subtotal = subtotal + float(product[PRICE_INDEX]) * float(row[NAME_INDEX])
                receipt = receipt + product[NAME_INDEX] + ": " + row[NAME_INDEX] + " @ " + product[PRICE_INDEX] + "\n"
    except FileNotFoundError as file_err:
            print(f"File not found error: {file_err}")
            return
    except PermissionError as perm_err:
            print(f"Permission error: {perm_err}")
            return
    except KeyError as key_err:
         print(f"Key error: {key_err}")
         return
    
    sale_tax = subtotal * .06
    total = subtotal + sale_tax
    """Receipt"""
    print("Gabriel Emporium")
    print(receipt)
    print(f"Number of Items: {number_item}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sale_tax:.2f}")
    print(f"Total: {total:.2f}")
    print("Thank you for shopping at the Gabriel Emporium.")
    print(today)


  

if __name__ == "__main__" :
    main()
