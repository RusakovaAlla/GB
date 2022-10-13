
encoded = str() #сюда будем записывать закодированную строку
count_encoded = 1 #счетчик для повторяющихся элементов

with open("encode.txt", "r") as file:
    string_to_encode = file.read()

for pos, elem in enumerate(string_to_encode[:-1]):
    if string_to_encode[pos] == string_to_encode[pos+1]:
            count_encoded += 1
    else:
        encoded += str(count_encoded)+elem
        count_encoded = 1



print(encoded)