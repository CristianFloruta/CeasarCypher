from encrypt_decrypt import encrypt, decrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

coding_messages_on = True

while coding_messages_on:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  
  if direction == "encode":
    
    text = input("Type your message:\n").lower()
    
    shift = int(input("Type the shift number:\n"))
  
    encrypt(plain_text=text, shift_amount=shift)

    play_on = input("Type 'yes' to continue, type 'no' to exit:\n").lower()

    if play_on == "no":

      coding_messages_on = False

    else:

      pass

  elif direction == "decode":

    text = input("Type your message:\n").lower()
    
    shift = int(input("Type the shift number:\n"))

    decrypt(plain_text=text, shift_amount=shift)

    play_on = input("Type 'yes' to continue, type 'no' to exit:\n").lower()

    if play_on == "no":

      coding_messages_on = False

    else:

      pass
