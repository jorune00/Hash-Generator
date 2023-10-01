#!/usr/bin/env python
# Password or key generator
# jorune00 -- 2023-09-29 10:26:14

import random, sys

def generate_hex_string(length=40):
    hex_chars = "0123456789abcdefABCDEF"
    return ''.join(random.choice(hex_chars) for _ in range(length))

def generate_binary_string(length=40):
    binary_chars = "01"
    return ''.join(random.choice(binary_chars) for _ in range(length))

def generate_alphanumeric_string(length=40):
    alphanumeric_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

def generate_alphanumeric_string_with_special_chars(length=40):
    alphanumeric_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

def generate_alphanumeric_string_with_special_chars_and_spaces(length=40):
    alphanumeric_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=- "
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

def generate_alphanumeric_string_with_special_chars_and_spaces_and_punctuation(length=40):
    alphanumeric_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=- ,.<>/?;:'\"[]{}\\|`~"
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

def hash_password_generator():
    """Generate a hash password based on user input"""

    # Validate selection input

    selection_flag = True
    while selection_flag:
        selection = input('''
                          
        \nWelcome to the Hash Password or Key Generator!

    Please select an option:
    1. Generate a hash with hex characters only
    2. Generate a hash with binary characters only
    3. Generate a hash with alphanumeric characters
    4. Generate a hash with alphanumeric characters and special characters
    5. Generate a hash with alphanumeric characters, special characters, spaces, and punctuation
    6. Exit

    Enter your choice (1-6): ''')
        if (selection == "1" or selection == "2" or selection == "3" or selection == "4" or selection == "5"):
            selection_flag = False
        elif selection == "6":
            end_program()
        else:
            print("Invalid selection. Please try again.")
            continue

    # Validate lenght input

    input_length_flag = True
    while input_length_flag:
        length = input("    Enter the length of the hash (default 40): ")
        if length == "":
            length = 40
            input_length_flag = False
        elif length.isdigit() and int(length) > 0:
            length = int(length)
            input_length_flag = False
        else: 
            print("Invalid length. Please try again.")
            continue

    # Generate hash based on selection

    if selection == "1":
        results = generate_hex_string(length)
        return results

    elif selection == "2":
        results = generate_binary_string(length)
        return results

    elif selection == "3":
        results = generate_alphanumeric_string(length)
        return results

    elif selection == "4":
        results = generate_alphanumeric_string_with_special_chars(length)
        return results

    elif selection == "5":
        results = generate_alphanumeric_string_with_special_chars_and_spaces_and_punctuation(length)
        return results

def end_program():
    """End the program"""

    print("\n<End of Line>\n")
    sys.exit()

# Main program

if __name__ == "__main__":
    results = hash_password_generator()
    print(f"\nYour hash is: {results}\n")
    end_program()

