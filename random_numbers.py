# Gabriel Nehemias Rengifo
#W04 Code-along Activity: Lists

import random
words = ["big", "red", "funny", "baby", "yellow", "wait", "python", "joseph" ]

def main():
    numbers = [16.2, 71.1, 52.3]
    word_list=[]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,3)
    print(numbers)
    append_random_words(word_list)
    print(word_list)
    append_random_words(word_list, 4)
    print(word_list)




def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):      
        num = round(random.uniform(0,100),1)
        numbers_list.append(num)


def  append_random_words(w_list, quantity=1):
    for _ in range (quantity):
        w_list.append(random.choice(words))


if __name__ == "__main__":
    main()



