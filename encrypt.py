alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):

    shifted_alphabet = alphabet.copy()

    for num in range(shift_amount):
        shifted_alphabet.insert(0, shifted_alphabet[-1])
        shifted_alphabet.pop()

    encoded_text = ''

    for letter in plain_text:
        position = alphabet.index(letter)
        encoded_text += shifted_alphabet[position]

    return encoded_text

