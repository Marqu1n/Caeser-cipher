alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input(
    'Type "encode" to encrypt, type "decode" to decrypt with a key or "brute force" to brute force it:\n'
)
text = input("Type your message:\n").lower()
if direction != "brute force":
    shift = int(input("Type the shift number:\n"))


def encrypt(msg, num):
    encrypted_msg = ""

    for i in msg:
        if i in alphabet:
            new_index = alphabet.index(i) + num
            new_index %= len(alphabet)
            encrypted_msg += alphabet[new_index]
        else:
            encrypted_msg += i
    print(f"this is the encrypted message: {encrypted_msg}")


def decrypt(msg, num):

    decrypted_msg = ""
    for i in msg:
        if i in alphabet:
            new_index = alphabet.index(i) - num
            new_index %= len(alphabet)
            decrypted_msg += alphabet[new_index]
        elif i not in alphabet:
            decrypted_msg += i
    print(f"this is the decrypted message: {decrypted_msg}")


def brute_force(msg):
    messages = {}

    j = 0
    while j < len(alphabet):
        encrypted_msg = ""
        for i in msg:
            if i in alphabet:
                new_index = alphabet.index(i) + j
                new_index %= len(alphabet)
                encrypted_msg += alphabet[new_index]
                messages[j] = encrypted_msg
            elif i not in alphabet:
                encrypted_msg += i
        j += 1

    print(f"these are the possibilities:{messages}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
elif direction == "brute force":
    brute_force(text)
else:
    print(f"Invalid entry: {direction}")
