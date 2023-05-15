alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
method = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    """takes the 'text' and shift each letter of the 'text' forwards in the
    alphabet by the shift amount
    """
    encoded_text = ''
    for letter in text:
        letter_index = alphabet.index(letter)
        new_index = letter_index + shift
        try:
            new_letter = alphabet[new_index]
        except IndexError:
            new_letter = alphabet[new_index % len(alphabet)]
        encoded_text += new_letter
    return encoded_text