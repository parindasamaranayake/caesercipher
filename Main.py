import string
from tkinter import *
from tkinter import ttk

# Arrays
letters = []
input_letters = []
cipher_text = []
plain_text = []

# Functions
def encryption():
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
def decryption():
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
def encrypt():
    try:
        user_input = plain_text_in.get().upper()
        for letter1 in user_input:
            input_letters.append(letter1)
        encryption()
        cipher_text_out.config(text=cipher_text)
    except ValueError:
        cipher_text_out.config(text="Please enter letters only.")
def decrypt():
    try:
        user_input = cipher_text_in.get().upper()
        for letter2 in user_input:
            input_letters.append(letter2)
        decryption()
        plain_text_out.config(text=plain_text)
    except ValueError:
        plain_text_out.config(text="Please enter letters only.")
def reset():
    window.update_idletasks()
    input_letters.clear()
    plain_text.clear()
    cipher_text.clear()
    plain_text_in.delete(0, END)
    cipher_text_in.delete(0, END)
    cipher_text_out.config(text="")
    plain_text_out.config(text="")

# Assigning English alphabet in to a list
upper_letters = string.ascii_uppercase
for letter in upper_letters:
    letters.append(letter)

# GUI
window = Tk()
window.geometry("400x100")
window.title("Caesar Cipher")
window.resizable(width=False, height=False)

notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Encryption")
notebook.add(tab2, text="Decryption")
notebook.pack(expand=1, fill="both")

# Tab 1
plain_label = Label(tab1, text="Plain Text ")
plain_label.place(x=4, y=4)

plain_text_in = Entry(tab1, width=40)
plain_text_in.place(x=73, y=4)

encrypt_button = Button(tab1, text="Encrypt", command=encrypt)
encrypt_button.place(x=330, y=4)

reset_button = Button(tab1, text="Reset", command=reset)
reset_button.place(x=330, y=40)

cipher_label = Label(tab1, text="Cipher Text")
cipher_label.place(x=4, y=40)

cipher_text_out = Label(tab1, bg="white", width=34)
cipher_text_out.place(x=73, y=40)

# Tab 2
cipher_label = Label(tab2, text="Cipher Text ")
cipher_label.place(x=4, y=0)

cipher_text_in = Entry(tab2, width=40)
cipher_text_in.place(x=73, y=0)

decrypt_button = Button(tab2, text="Decrypt", command=decrypt)
decrypt_button.place(x=330, y=0)

reset_button = Button(tab2, text="Reset", command=reset)
reset_button.place(x=330, y=40)

plain_label = Label(tab2, text="Plain Text")
plain_label.place(x=4, y=40)

plain_text_out = Label(tab2, bg="white", width=34)
plain_text_out.place(x=73, y=40)

window.mainloop()