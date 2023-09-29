#!/usr/bin/env python
# jorune00 -- 2023-09-29 10:26:14

import random

def generate_even_hex_string(length=40):
    hex_chars = "02468aceACE"
    return ''.join(random.choice(hex_chars) for _ in range(length))

# Generate a 40-character hash with even hex characters only

print("\nGenerate a 40-character hash with even hex characters only\n" +
      "--------------------------------------------------------")
length = input("Enter the length of the hash (default 40):")
if length == "":
    length = 40
else:
    length = int(length)
results = generate_even_hex_string(length)
print(results)