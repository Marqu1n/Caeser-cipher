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



def allinone():

  correct_direction = False
  while not correct_direction:
    direction = input(
    'Escolha entre codificar, decodificar e força bruta:\n'
)  
    if direction == "codificar":
      correct_direction = True
      text = input("Type your message:\n").lower()
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
        print(f"Essa é a mensagem codificada: {encrypted_msg}")
      encrypt(text, shift)

    elif direction == "decodificar":
      correct_direction = True
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      def decrypt(msg, num):
        decrypted_msg = ""
        for i in msg:
          if i in alphabet:
            new_index = alphabet.index(i) - num
            new_index %= len(alphabet)
            decrypted_msg += alphabet[new_index]
          elif i not in alphabet:
            decrypted_msg += i
        print(f"Essa é a mensagem decodificada: {decrypted_msg}")
      decrypt(text, shift)

    elif direction == "força bruta":
      correct_direction = True
      text = input("Type your message:\n").lower()
      
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
        print(f"Essas são todas as possibilidades:{messages}")
      brute_force(text)

    else:
      raise ValueError('\nValor inválido!\nRode o código novamente')

allinone()