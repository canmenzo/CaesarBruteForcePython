LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Read the encrypted message from a file
filename = 'encrypted_message.txt'  # Replace with your file name
with open(filename, 'r') as file:
    message = file.read()

# Decrypt the message
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Decrypted message #%s: %s' % (key, translated))
