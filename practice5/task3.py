def encode_string(some_file):
    """кодирование"""
    encoded = str() #сюда будем записывать закодированную строку
    count_encoded = 1 #счетчик для повторяющихся элементов
    with open(some_file, "r") as file:
        string_to_encode = file.read() #читаем строку
    for pos, elem in enumerate(string_to_encode):
        if pos != len(string_to_encode) - 1:
            if string_to_encode[pos] == string_to_encode[pos+1]:
                count_encoded += 1
            else:
                encoded += str(count_encoded)+elem
                count_encoded = 1
        else:
            if string_to_encode[pos] == string_to_encode[pos-1]:
                encoded += str(count_encoded) + elem
            else:
                count_encoded = 1
                encoded += str(count_encoded) + elem
    file_name = str(input(f"Задайте имя закодированного файла: "))
    with open(f"{file_name}.txt", "w") as file:
        file.write(encoded)

    return encoded
encode_string("to_encode.txt")

def decode_string(some_file):
    """раскодирование"""
    decoded = str()#сюда будем записывать закодированную строку
    try:
        with open(some_file, "r") as file:
            string_to_decode = file.read() #читаем строку
    except:
        pass
    while string_to_decode:
        for pos, elem in enumerate(string_to_decode):
            if not elem.isdigit():
                number = int(string_to_decode[0:pos])
                decoded += elem * number
                string_to_decode = string_to_decode[string_to_decode.find(elem)+1:]
                break
            else:
                pass
    file_name = str(input(f"Задайте имя раскодированного файла: "))
    with open(f"{file_name}.txt", "w") as file:
        file.write(decoded)

    return decoded

decode_string("encoded53.txt")


