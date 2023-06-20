LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def encrypt_message(message, key):
    encrypted = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = (num + key) % len(LETTERS)
            encrypted += LETTERS[num]
        else:
            encrypted += symbol
    return encrypted

# Prompt the user for input
message = input("Enter the message to encrypt: ")
key = int(input("Enter the encryption key (a non-negative integer): "))

# Encrypt the message
encrypted_message = encrypt_message(message, key)
print("Encrypted message:", encrypted_message)

# Save the encrypted message to a file
filename = "encrypted_message.txt"
with open(filename, "w") as file:
    file.write(encrypted_message)

print(f"Encrypted message saved to {filename}.")
