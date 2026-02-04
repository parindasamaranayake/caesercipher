import string

# Arrays
letters = []
input_letters = []
cipher_text = []
plain_text = []

# Functions
def encrypt():
    for input_letter in input_letters:
        if input_letter == " ":
            cipher_text.append(" ")
        else:
            position = letters.index(input_letter)
            if (position + 3) <= (len(letters) - 1):
                cipher_text.append(letters[position + 3])
            else:
                new_position = (position + 3) - 25
                cipher_text.append(letters[new_position - 1])
def decrypt():
    for input_letter in input_letters:
        if input_letter == " ":
            plain_text.append(" ")
        else:
            position = letters.index(input_letter)
            if (position - 3) >= 0:
                plain_text.append(letters[position - 3])
            else:
                new_position = 26 + (position - 3)
                plain_text.append(letters[new_position])

# Assigning English alphabet in to a list
upper_letters = string.ascii_uppercase
for letter in upper_letters:
    letters.append(letter)

method = input("Enter your method (encrypt or decrypt): ")

if method == "encrypt":
    user_input = input("Enter your word : ").upper()
    for letter in user_input:
        input_letters.append(letter)
    encrypt()
    print("Cipher text: ", end="")
    for letter in cipher_text:
        print(letter, end="")

elif method == "decrypt":
    user_input = input("Enter your word : ").upper()
    for letter in user_input:
        input_letters.append(letter)
    decrypt()
    print("Plain text: ", end="")
    for letter in plain_text:
        print(letter, end="")