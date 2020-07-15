import os
small_alpha = 'abcdef01289ghijPRSklop;\'<|>,.qr st3Q45NOmnTUVWX67uvwxyzABCDEFGH~`+_)(*&^%$#@!-=IJKLMYZ{[}]:"?/\\'

def encrypt(data):

    user_input = data
    forword_str_char_by = 69
    string_len = len(user_input)
    output = ""

    for i in range(string_len):
        char = user_input[i]
        if small_alpha.find(char) != -1:
            location_of_char = small_alpha.find(char)
            new_location = (location_of_char + forword_str_char_by) % 94
            output = output + small_alpha[new_location]

    return output

def decrypt(data):

    user_input = data
    forword_str_char_by = 69
    string_len = len(user_input)
    actual = ""

    for i in range(string_len):
        char = user_input[i]
        location_of_char = small_alpha.find(char)
        new_location = (location_of_char - forword_str_char_by) % 94
        actual = actual + small_alpha[new_location]

    return actual

def de_file(file_name):
    fil1 = open(file_name, "r")
    r = fil1.read()
    a = decrypt(r)
    fil1.close()
    os.remove(file_name)
    #######################
    fil1 = open(file_name, "w")
    fil1.write(a)
    fil1.close()


def en_file(file_name):
    fil1 = open(file_name, "r")
    r = fil1.read()
    a = encrypt(r)
    fil1.close()
    os.remove(file_name)
    #######################
    fil1 = open(file_name, "w")
    fil1.write(a)
    fil1.close()

