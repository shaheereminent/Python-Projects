print(12 *- 1)
#alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

#if direction == "encode":
#    text = input("What message would you like to encrypt: ").lower()
#elif direction == "decode":
#    text = input("Write your message to Decrypt: ").lower()
    
#shift = int(input("Type the shift number: "))

#def caeser(plain_text, shift_number):
#    message = ""
#    if direction == "encode":
#        for letter in plain_text:
#            current_position = alphabet.index(letter)
#            new_position = current_position + shift_number
#            encoded_letter = alphabet[new_position]
#            message += encoded_letter
#        print(f"Your encoded message is: {message}")
#    elif direction == "decode":
#        for letter in plain_text:
#            current_position = alphabet.index(letter)
#            new_position = current_position - shift_number
#            decoded_letter = alphabet[new_position]
#            message += decoded_letter
#        print(f"Your decoded message is: {message}")
#        
#caeser(plain_text = text, shift_number = shift)
            
        

#def encrypt(plain_text, shift_number):
#    encoded_message = ""
#    for letter in plain_text:
#        position_of_letter = alphabet.index(letter)
#        new_letter_position = position_of_letter + shift_number
#        new_letter = alphabet[new_letter_position]
#        encoded_message += new_letter
#    print(f"Your encoded message is: {encoded_message}")
    
#def decrypt(plain_text, shift_number):
#    decoded_message = ""
#    for letter in plain_text:
#        position_of_letter = alphabet.index(letter)
#        new_letter_position = position_of_letter - shift_number
#        new_letter = alphabet[new_letter_position]
#        decoded_message += new_letter
#    print(f"Your decoded message is: {decoded_message}")

#if direction == "encode":
#    encrypt(plain_text = text, shift_number = shift)
#else:
#    decrypt(plain_text = text, shift_number = shift)
    