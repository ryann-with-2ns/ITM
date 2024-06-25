def shift_letter(letter, shift):
    
    alphabet_shift_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return " "
    elif alphabet_shift_letter.find(letter) + shift > 25:
        return alphabet_shift_letter[alphabet_shift_letter.find(letter) + shift - (26*((alphabet_shift_letter.find(letter) + shift)//26))]
    else:
        return alphabet_shift_letter[alphabet_shift_letter.find(letter) + shift]

def caesar_cipher(message, shift):
    
    alphabet_caesar_cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index_number_message_caesar_cipher = 0
    new_string_caesar_cipher = ""
    while index_number_message_caesar_cipher <= len(message) - 1:
        if message[index_number_message_caesar_cipher] == " ":
            new_string_caesar_cipher += " "
            index_number_message_caesar_cipher += 1
        elif alphabet_caesar_cipher.find(message[index_number_message_caesar_cipher]) + shift > 25:
            new_string_caesar_cipher += alphabet_caesar_cipher[alphabet_caesar_cipher.find(message[index_number_message_caesar_cipher]) + shift - (26*((alphabet_caesar_cipher.find(message[index_number_message_caesar_cipher]) + shift)//26))]
            index_number_message_caesar_cipher += 1
        else:
            new_string_caesar_cipher += alphabet_caesar_cipher[alphabet_caesar_cipher.find(message[index_number_message_caesar_cipher]) + shift]
            index_number_message_caesar_cipher += 1
    return new_string_caesar_cipher

def shift_by_letter(letter, letter_shift):

    alphabet_shift_by_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_shift = alphabet_shift_by_letter.index(letter_shift)
    if letter == " ":
        return " "
    elif alphabet_shift_by_letter.find(letter) + letter_shift > 25:
        return alphabet_shift_by_letter[alphabet_shift_by_letter.find(letter) + letter_shift - (26*((alphabet_shift_by_letter.find(letter) + letter_shift)//26))]
    else:
        return alphabet_shift_by_letter[alphabet_shift_by_letter.find(letter) + letter_shift]

def vigenere_cipher(message, key):

    # input_cleaner
    if len(message) - len(key) > 0:
        key = key + (key * ((len(message) - len(key)) // len(key))) # whole word repition/s of the key
        for i in range(0, ((len(message)-len(key)) % len(key))): # cut off repitition of the key
            key += key[i]

    # vigenere cipher itself
    alphabet_vigenere_cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index_number_message_vigenere_cipher = 0
    new_string_vigenere_cipher = ""
    while index_number_message_vigenere_cipher <= len(message) - 1:
        if message[index_number_message_vigenere_cipher] == " ":
            new_string_vigenere_cipher += " "
            index_number_message_vigenere_cipher += 1
        elif alphabet_vigenere_cipher.find(message[index_number_message_vigenere_cipher]) + alphabet_vigenere_cipher.index(key[index_number_message_vigenere_cipher]) > 25:
            new_string_vigenere_cipher += alphabet_vigenere_cipher[alphabet_vigenere_cipher.find(message[index_number_message_vigenere_cipher]) + alphabet_vigenere_cipher.index(key[index_number_message_vigenere_cipher]) - (26*((alphabet_vigenere_cipher.find(message[index_number_message_vigenere_cipher]) + alphabet_vigenere_cipher.index(key[index_number_message_vigenere_cipher]))//26))]
            index_number_message_vigenere_cipher += 1
        else:
            new_string_vigenere_cipher += alphabet_vigenere_cipher[alphabet_vigenere_cipher.find(message[index_number_message_vigenere_cipher]) + alphabet_vigenere_cipher.index(key[index_number_message_vigenere_cipher])]
            index_number_message_vigenere_cipher += 1
    return new_string_vigenere_cipher

def scytale_cipher(message, shift):

    # input cleaner
    new_message_scytale_cipher = ""
    i = 0

    if len(message) % shift == 0:
        message = message
    else:
        message = message + ("_" * (shift - (len(message) % shift)))

    # cipher itself
    while i <= len(message) - 1:
        new_message_scytale_cipher += message[(i // shift) + (len(message) // shift) * (i % shift)]
        i += 1
    return new_message_scytale_cipher
    
def scytale_decipher(message, shift):
    
    new_message_scytale_decipher = ""
    i = 0
    while i <= len(message) - 1:
        new_message_scytale_decipher += message[(i % (len(message) // shift)) * shift + (i // (len(message)// shift))]
        i += 1
    return new_message_scytale_decipher