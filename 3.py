def encode_dna_sequence(s):
    encoded_string = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_string.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    encoded_string.append(f"{current_char}{count}")
    
    return "".join(encoded_string)


dna_sequence = input("Введите строку ДНК:")
print(encode_dna_sequence(dna_sequence))