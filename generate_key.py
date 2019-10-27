import string

def generate_key(start_letter, decodeflag):

    key={}
    std_string = string.ascii_lowercase
    start_pos = std_string.index(start_letter)
    new_string = std_string[start_pos: 26]+ std_string[0:start_pos]
    
    for i in range(26):
        if decodeflag == True:
            key[new_string[i]] = std_string[i]
        else:
            key[std_string[i]] = new_string[i]

    return(key)
