---

# Hash Password or Key Generator

## Overview

This Python script provides a menu-driven interface for generating secure hashes or keys based on user-defined criteria. The generated hash can contain different types of characters, including:

- Hexadecimal characters
- Binary characters
- Alphanumeric characters
- Special characters
- Spaces and punctuation

## Requirements

- Python 3.x

## How to Use

1. Run the script in your terminal.
    ```
    python hash_pw_generator.py
    ```
2. The script will display a menu with options to generate different types of hashes.
3. Choose the desired hash type by entering the corresponding number.
4. Next, specify the length of the hash. Default length is 40 characters.
5. The script will generate the hash and display it.

## Functions

### `generate_hex_string(length=40)`

Generates a hash containing only hexadecimal characters.

### `generate_binary_string(length=40)`

Generates a hash containing only binary characters.

### `generate_alphanumeric_string(length=40)`

Generates a hash containing alphanumeric characters.

### `generate_alphanumeric_string_with_special_chars(length=40)`

Generates a hash containing alphanumeric and special characters.

### `generate_alphanumeric_string_with_special_chars_and_spaces(length=40)`

Generates a hash containing alphanumeric characters, special characters, and spaces.

### `generate_alphanumeric_string_with_special_chars_and_spaces_and_punctuation(length=40)`

Generates a hash containing alphanumeric characters, special characters, spaces, and punctuation.

## License

This project is open-source. Feel free to modify or distribute.

## Author

- jorune00

---