def caesar_cipher(text, shift, operation):
    result = ""

    if operation.lower() == 'decrypt':
        shift = -shift

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

t=int(input("enter the number of test cases:"))
for i in range(t):
        m = input("Enter a message: ")
        value = int(input("Enter the shift value: "))
        operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt the message: ")

        rmessage = caesar_cipher(m,value,operation)

        print(f"The resulting message is: {rmessage}")
