#!/usr/bin/env python
# Password generator
# jorune00 -- 2023-09-29 10:26:14

import random

def generate_hex_string(length=40):
    hex_chars = "02468aceACE"
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

    selection = input('''\nWelcome to the Hash Password Generator!

    Please select an option:
    1. Generate a hash with hex characters only
    2. Generate a hash with binary characters only
    3. Generate a hash with alphanumeric characters
    4. Generate a hash with alphanumeric characters and special characters
    5. Generate a hash with alphanumeric characters, special characters, spaces, and punctuation
    6. Exit

    Enter your choice (1-6): ''')

    if selection == "1":
        length = input("Enter the length of the hash (default 40):")
        if length == "":
            length = 40
        else:
            length = int(length)
        results = generate_hex_string(length)
        return results

    elif selection == "2":
        length = input("Enter the length of the hash (default 40):")
        if length == "":
            length = 40
        else:
            length = int(length)
        results = generate_binary_string(length)
        return results

    elif selection == "3":
        length = input("Enter the length of the hash (default 40):")
        if length == "":
            length = 40
        else:
            length = int(length)
        results = generate_alphanumeric_string(length)
        return results

    elif selection == "4":
        length = input("Enter the length of the hash (default 40):")
        if length == "":
            length = 40
        else:
            length = int(length)
        results = generate_alphanumeric_string_with_special_chars(length)
        return results

    elif selection == "5":
        length = input("Enter the length of the hash (default 40):")
        if length == "":
            length = 40
        else:
            length = int(length)
        results = generate_alphanumeric_string_with_special_chars_and_spaces_and_punctuation(length)
        return results

    elif selection == "6":
        results = "Goodbye!"
        return results

    else:
        results = "Invalid selection. Please try again."
        return results

# Main program

flag = True

while flag:
    results = hash_password_generator()
    if results == "Goodbye!":
        print(f"\n{results}\n")
        break
    else:
        print(f"\n{results}\n")
        continue
    
