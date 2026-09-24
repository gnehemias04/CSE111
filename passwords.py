
"""W02 Project: Password Strength
   Author: Gabriel Nehemias Rengifo Krunfli
   Course: wdd130
"""

#Global Variables
lower=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
digits=["0","1","2","3","4","5","6","7","8","9"]
special=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]




def word_in_file (word, filename, case_sensitive=False) :
    
    with open (filename, "r", encoding="utf-8") as file:
         filetxt = file.readlines()



    for line in filetxt:
        if case_sensitive == False :
            if word.lower() == line.strip().lower() :
                return True
        elif case_sensitive == True :
            if word == line.strip() :
                return True
                

    return False
        
        
    

def word_has_character(word, character_list):

    for letter in word:
         if letter in character_list :
             return True

    return False

def word_complexity(word):
    value = 0
    if word_has_character(word, lower) :
        value += 1
    if word_has_character(word, upper) :
        value += 1
    if word_has_character(word, digits) :
        value +=1
    if word_has_character (word, special) :
        value +=1
    return value

def password_strength(password, min_length=10, strong_length=16):
#chech if the password is a dictionary word
    if word_in_file(password, "wordlist.txt") ==  True :
        print("Password is a dictionary word and is not secure.")
        return 0

#chech if the password is a known password
    if word_in_file(password, "toppasswords.txt") ==  True :
            print("Password is a commonly used password and is not secure.")
            return 0

    if len(password) < min_length :
        print("Password is too short and is not secure.") 
        return 1

    if len(password) >= strong_length :
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    
    result = word_complexity(password) + 1
    
    return result

def main():
    word = ""
    print("Hello, thanks for using the Password Strength! This program will help you find the stronger password for you!")
    while word.lower() !="q":
        word = input("New password: ")
        if word.lower() != "q" :
            result = password_strength(word)
            print(f"Strength: {result}")
            print("Type 'q' or 'Q' to exit")
        
    print ("Thanks For using the Password Strength")

if __name__ == "__main__":
    main()