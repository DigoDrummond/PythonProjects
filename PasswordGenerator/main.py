import random
import string

def generate_password(min_length, numbers=True,special_characters=True):
    letters = string.ascii_letters# gets all the letters
    digits = string.digits #gets all the digits
    special = string.punctuation #gets all the special caraters
    #print(letters,digits,special)
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd


def main():
    min_length = int(input("Enter the minimum length of your new password: "))
    has_number = input("Do you want to have numbers in your password? (y/n): ").lower() == "y"#return boolean
    has_special = input("Do you want you have special caraters in your password? (y/n): ").lower() == "y"
    password = generate_password(min_length, has_number,has_special)
    print(f"The generated password is: {password}")
    
main()