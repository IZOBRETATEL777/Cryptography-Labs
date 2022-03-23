#!/bin/python3

# Length of classic ASCII is 128 symbols
ALPHABET_LENGTH = 128


# Returns the modular inverse using the Extended Euclidean Algorithm:
def findModInverse(a, m):
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# Function that decrypts message (recurent)
def decryptMessage(message: str, keyA: int, keyB: int, currentEncrypted="", currentMessageIdx = 0):
    # Recursion base case (when we finished the work with string)
    if currentMessageIdx == len(message):
        return currentEncrypted
    # Use (x - b) * a^-1 % len_of_alphabet formula where a^-1 is inverse mode of a and len_of_alphabet
    currentEncrypted += chr((ord(message[currentMessageIdx]) - keyB) * findModInverse(keyA, ALPHABET_LENGTH) % ALPHABET_LENGTH)
    return decryptMessage(message, keyA, keyB, currentEncrypted, currentMessageIdx+1)


if __name__ == '__main__':
    pass
