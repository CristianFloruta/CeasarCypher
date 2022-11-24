from encrypt import encrypt
from decrypt import decrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypted_message = encrypt(plain_text = text, shift_amount = shift)
print(f' Your encrypted code is: {encrypted_message} \n')


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

decripted_message = decrypt(encoded_text = text, shift_amount = shift)
print(f' Your decrypted code is: {decripted_message} ')





