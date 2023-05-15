from art import logo


print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_decrypt(cipher_method, text_message, shift_amount):
    """takes the 'text_message' and shift each letter forwards or
    backwards in the alphabet by the 'shift_amount'
    """
    new_text = ''
    if cipher_method == 'decode':
        shift_amount *= -1
    for letter in text_message:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_index = letter_index + shift_amount
            try:
                new_letter = alphabet[new_index]
            except IndexError:
                new_letter = alphabet[new_index % len(alphabet)]
            new_text += new_letter
        else:
            new_text += letter
    print(f'message after modification: {new_text}')


continuation = True
while continuation:
    text = input("Type your message:\n").lower()
    method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    shift = int(input("Type the shift number:\n"))
    encrypt_decrypt(cipher_method=method, text_message=text,
                    shift_amount=shift)
    print('--------------------------------------------------------------')
    decision = input('If you want to play again type "yes" ale type "no": ')
    if decision == 'no':
        continuation = False
        print('goodbye')
