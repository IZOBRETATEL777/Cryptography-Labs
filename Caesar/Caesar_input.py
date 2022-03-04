#!/bin/python3

# Encryption recursive function
def encrypt(message, key, idx = 0):
    if idx == len(message): #if index of current char is equal to the size of string
        return message; # encryption of has finished
    if not message[idx].isspace(): # skip all space and tabs
        ch = message[idx]
        if ch.isupper():
            ch = chr((ord(ch) + key - ord('A')) % 26 + ord('A')) # main formula
        else:
            ch = chr((ord(ch) + key - ord('a')) % 26 + ord('a'))
        message = message[:idx] + ch + message[idx + 1:]
    return encrypt(message, key, idx + 1)


# The same for the decryption
def decrypt(message, key, idx = 0):
    if idx == len(message):
        return message;
    if not message[idx].isspace():
        ch = message[idx]
        if ch.isupper(): # But it is decrypting formula
            ch = chr((ord(ch) - key - ord('A')) % 26 + ord('A'))
        else:
            ch = chr((ord(ch) - key - ord('a')) % 26 + ord('a'))
        message = message[:idx] + ch + message[idx + 1:]
    return decrypt(message, key, idx + 1)


# Exceptions handling
def isValidInput(text, key):
    if any(not (i.isalpha() or i.isspace()) for i in text):
        print('Only alpahabets are allowed!')
        return False
    if not 0 <= key <= 26:
        print('Key is out of range')
        return False
    return True


# Driver code
while True:
    # Menu output
    print('1.Encryption\n2.Decryption\n3.Exit')
    cmd = int(input("Choose(1,2,3): "))
    if cmd == 1:
        print('Encryption')
        print('Message can be only Lower or Upper alphabet')
        msg = input('Enter message: ')
        key = int(input('Enter key(0-26): '))
        # Validate input
        if not isValidInput(msg, key):
            continue
        enc = encrypt(msg, key)
        print(enc)
    elif cmd == 2:
        print('Decryption')
        enc = input('Enter encrypted text: ')
        key = int(input('Enter key(0-26): '))
        # Validate input
        if not isValidInput(enc, key):
            continue
        msg = decrypt(enc, key)
        print(msg)
    elif cmd == 3:
       print('Bye!')
       break
    else:
        print('I do not know this command')
        continue

