def decode(file):
    width = get_width(file)
    height = get_height(file)
    offset = get_offset(file)
    file.seek(offset)

    string = ""
    current_char = 0
    current_byte = 0
    
    for byte in range(1,width * height * 3):
            
        b = file.read(1)[0] & 1
        current_char += b << current_byte
        current_byte += 1
        
        if (current_byte == 8):
            if (current_char == 0):
                break
            string += chr(current_char)
            current_byte = 0
            current_char = 0

    print(string)

def encode():
    pass

def get_thing(file):
    b = file.read(4)
    thing = 0
    for i in range(len(b)):
        thing += 256 ** i * b[i]
    return thing
                      
def get_width(file):
    file.seek(18)
    return get_thing(file)

def get_height(file):
    file.seek(22)
    return get_thing(file)

def get_offset(file):
    file.seek(10)
    return get_thing(file)

file = open("ncss-modified.bmp","rb")
decode(file)
