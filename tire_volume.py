# W01 Project: Tire Volume
# Milestones 
# I add the option to buy a tire if the user wants. also I add some prices for 6 tire width
import math 
from datetime import datetime
prices = [(205,"$100"),(195,"$90"),(175,"$85"),(215,"$110"),(225,"$130"),(235,"$140") ]


today = datetime.now()
day= today.date()
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_radio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = (math.pi * width ** 2 * aspect_radio * (width * aspect_radio + 2540 * diameter)) / 10000000000
data = str(day) + ", " + str(width) +", " + str(aspect_radio) +", " + str(diameter) +", " +  f"{volume:.2f}"
print (f"The approximate volume is {volume:.2f} liters ")
print (data)

#Telling to the use the price of the tire

price = 0
if width == 205 :
    price = "$100"
    print(f"The price of the {width}/{aspect_radio} r{diameter} is {price}" )
elif width == 195:
    price ="$90"
    print(f"The price of the {width}/{aspect_radio} r{diameter} is {price}")
elif width == 175:
    price ="$85"
    print(f"The price of the {width}/{aspect_radio} r{diameter} is {price}" )
elif width == 215:
    price ="$110"
    print(f"The price of the {width}/{aspect_radio} r{diameter} is {price}" )
elif width == 225:
    price ="$130"
    print(f"The price of the {width}/{aspect_radio} r{diameter} is {price}" )
elif width == 235:
    price ="$140"
    print(f"The price of the {width}/{aspect_radio} r{diameter} is {price}" )
else :
    print("Sorry, we don't have any stock for this {width}/{aspect_radio} r{diameter} is {price} ")

#Asking the user if He/She wants to buy the tire and put the phone number
cell_number = ""

buy_confirmation = input("Do you want to buy the tire? (yes/no) ")
if buy_confirmation == "yes" :
    cell_number = input("Perfect, what is your telephone numeber to send you more information about your purchase? ")
    print("Thanks, in a few moments we will send you a message with more information.")
elif buy_confirmation == "no" :
    print("Okey!")

#here we are storaging the information in a .txt file*/
with open ("volumes.txt", "a") as file :
    file.write(data + ", " + cell_number + "\n")