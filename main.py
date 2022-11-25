from encrypt import encrypt
from decrypt import decrypt
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

game_on = True

print(logo)

while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == 'encode':

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        encrypted_message = encrypt(plain_text=text, shift_amount=shift)
        print(f' Your encrypted code is: {encrypted_message} \n')

        once_again = input("Whould you like to continue? Type 'yes' or 'no':\n").lower()

        if once_again == 'yes':
            pass

        elif once_again == 'no':
            game_on = False

        else:
            once_again = input("Wrong entrance! Type 'yes' or 'no':\n").lower()

    elif direction == 'decode':

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        decripted_message = decrypt(encoded_text=text, shift_amount=shift)
        print(f' Your decrypted code is: {decripted_message} ')

        once_again = input("Whould you like to continue? Type 'yes' or 'no':\n").lower()

        if once_again == 'yes':
            pass

        elif once_again == 'no':
            game_on = False

        else:
            once_again = input("Wrong entrance! Type 'yes' or 'no':\n").lower()






