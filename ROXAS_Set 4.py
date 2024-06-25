def bin_to_dec(binary_string):
    
    base_10_number = 0
    reversed_binary = binary_string[::-1]
    digit_num = 0
    for digit_num in range(0,len(reversed_binary)):
        base_10_number += int(reversed_binary[digit_num])*(2**digit_num)
    return base_10_number

def dec_to_bin(number):

    length_of_string = 0
    a = 0
    binary_string = ""
    if number == 0:
        length_of_string = 1
    else:
        while 2**a <= number:
            length_of_string += 1
            a += 1

    while length_of_string > 0:
        if number - (2**(length_of_string-1)) >= 0:
            binary_string += "1"
            number = number - (2**(length_of_string-1))
        else:
            binary_string += "0"
        length_of_string -= 1
    return binary_string

def telephone_cipher(message):
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
    index_telephone_cipher = 0
    numerical_string = ""
    while index_telephone_cipher <= len(message) - 1:
        if index_telephone_cipher == 0:
            numerical_string += encoder_dict[message[index_telephone_cipher]]
        else:
            if encoder_dict[message[index_telephone_cipher]][0] == encoder_dict[message[index_telephone_cipher - 1]][0]:
                numerical_string += "_" + encoder_dict[message[index_telephone_cipher]]
            else:
                numerical_string += encoder_dict[message[index_telephone_cipher]]
        index_telephone_cipher += 1
    return numerical_string

def telephone_decipher(telephone_string):
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    index_word_separator = 0
    index_list_cleaner = 0
    index_letter_printer = 0
    cleaned_list = []
    separated_numbers = ""
    text_string = ""
    while index_word_separator <= len(telephone_string) - 1:
        if index_word_separator == 0:
            separated_numbers += telephone_string[index_word_separator]
        else:
            if telephone_string[index_word_separator] == telephone_string[index_word_separator - 1]:
                separated_numbers += telephone_string[index_word_separator]
            else:
                separated_numbers += " " + telephone_string[index_word_separator]
        index_word_separator += 1
    separated_numbers = separated_numbers.split()
    while index_list_cleaner <= len(separated_numbers) - 1:
        if separated_numbers[index_list_cleaner] != "_":
            cleaned_list.append(separated_numbers[index_list_cleaner])
        index_list_cleaner += 1
    while index_letter_printer <= len(cleaned_list) - 1:
        text_string += decipher_dict[cleaned_list[index_letter_printer]]
        index_letter_printer += 1
    return text_string