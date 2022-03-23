#!/bin/python3

# Length of classic ASCII is 128 symbols
ALPHABET_LENGTH = 128


# recurent function that encrypts mesage
def encryptMessage(message, keyA, keyB, currentEncrypted="", currentMessageIdx=0):
    # Recursion base case (when we finished the work with string)
    if currentMessageIdx == len(message):
        return currentEncrypted
    # use (ax + b) % len_of_alphabet formula to get appropriate ASCII code
    currentEncrypted += chr((ord(message[currentMessageIdx]) * keyA + keyB) % ALPHABET_LENGTH)
    return encryptMessage(message, keyA, keyB, currentEncrypted, currentMessageIdx+1)


if __name__ == '__main__':
    pass
