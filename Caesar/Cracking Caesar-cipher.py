#!/bin/python3

def decrypt(message, key, idx = 0):
    if idx == len(message):
        return message;
    if not message[idx].isspace():
        ch = message[idx]
        if ch.isupper(): # Using derypting formula
            ch = chr((ord(ch) - key - ord('A')) % 26 + ord('A'))
        else:
            ch = chr((ord(ch) - key - ord('a')) % 26 + ord('a'))
        message = message[:idx] + ch + message[idx + 1:]
    return decrypt(message, key, idx + 1)

#Driver code
enc = input('Enter encrypted message to bruteforce.\nOnly lower and capital letters are accepted: ')

#Exceptions
if any(not (i.isalpha() or i.isspace()) for i in enc):
    print('Read the message above again!')
    exit(0)

#Bruteforce approach
print('All possible variants:')
for key in range (1, 27):
    print(decrypt(enc, key))
