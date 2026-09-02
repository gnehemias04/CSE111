#W01 Prepare 2: Calling Functions
import math

number_items = int(input("Enter the number of items: "))
number_items_per_box = int(input("Enter the number of items per box: "))
boxes = number_items / number_items_per_box
boxes_ceil = math.ceil(boxes)

print(f"For {number_items} items, packing {number_items_per_box} items in each box, you will need {boxes_ceil} boxes.")