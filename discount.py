# W01 Code-along Activity: Discount

from datetime import datetime
discount_rate = 0.1
tax_rate = .06
today = datetime.now()
dow=today.weekday()
subtotal = 0
quantity = 1
while quantity != 0:
        quantity=int(input("Enter the quantity: "))
        if quantity !=0:
            price = float(input("Enter the price: "))
        subtotal += quantity * price
discount = 0
if dow == 1 or dow == 2 :
    if subtotal > 50:
        print(f"Discount {discount:.2f}")
        discount = round( subtotal * discount_rate, 2)
    else:
        short = 50 - subtotal
        print(f"You can get a discount by ordering {short:.2f} more. ")

print(f"Total Order {subtotal:.2f}")
subtotal = subtotal - discount
tax =round( subtotal * tax_rate, 2)
total = subtotal + tax

print (F"Tax {tax:.2f}")
print(f"Total due {total:.2f}")
