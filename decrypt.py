alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

def decrypt(encoded_text, shift_amount):

    shifted_alphabet = alphabet.copy()

    for num in range(shift_amount):
        shifted_alphabet.insert(0, shifted_alphabet[-1])
        shifted_alphabet.pop()

    decoded_text = ''

    for letter in encoded_text:
        position = shifted_alphabet.index(letter)
        decoded_text += alphabet[position]

    return decoded_text


