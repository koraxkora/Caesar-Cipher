alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
shift = int(input("Type the shift number:\n"))


def encrypt_decrypt(cipher_method = method, text_message = text, shift_amount = shift):
    """takes the 'text' and shift each letter of the 'text' forwards or
    backwards in the alphabet by the shift amount
    """
    new_text = ''
    if cipher_method == 'decode':
        shift_amount *= -1
    for letter in text_message:
        letter_index = alphabet.index(letter)
        new_index = letter_index + shift_amount
        try:
            new_letter = alphabet[new_index]
        except IndexError:
            new_letter = alphabet[new_index % len(alphabet)]
        new_text += new_letter
    return new_text

