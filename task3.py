#task 3

import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    length = max(length, 8)

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if (password_length <8):{
            print("\nWe only create 8 char or more then 8 char password \n ")
            
        }
        password = generate_password(password_length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()