alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

welcome = input("Enter 'encode' to encode or 'decode' to decode : ")
plain_input = input("Enter words to encode or decode : ")
shifting_number = int(input("Enter shifting number : "))

encoded_text = ""
valid_jump_position = 0
jump_position = 0

if welcome == "encode":
    for i in range(0,len(plain_input)):
        letter_to_encode = plain_input[i]
        for i in range(0,len(alphabet)):
            alphabet_letter = alphabet[i]
            if letter_to_encode == alphabet_letter:
                jump_position = i + shifting_number
                if jump_position >= 27:
                    valid_jump_position = jump_position - 27
                    encoded_text += alphabet[valid_jump_position]
                else:
                    encoded_text += alphabet[jump_position]
elif welcome == "decode":
    for i in range(0,len(plain_input)):
        letter_to_decode = plain_input[i]
        for i in range(0,len(alphabet)):
            alphabet_letter = alphabet[i]
            if letter_to_decode == alphabet_letter:
                jump_position = i - shifting_number
                if jump_position < 0:
                    valid_jump_position = 27 + jump_position
                    encoded_text += alphabet[valid_jump_position]
                else:
                    encoded_text += alphabet[jump_position]
else:
    print("Invalid input")
    
print(encoded_text)