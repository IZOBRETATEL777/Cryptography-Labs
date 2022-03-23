#!/bin/python3

# Imports with decryption and encryption functions that are used in main
from decrypt import decryptMessage, ALPHABET_LENGTH
from encrypt import encryptMessage

# For key cheking
from math import gcd

# For key generation
import string
import random

# Function that generate string of length n from ASCII letters and space
def generateRandomString(n):
    return ''.join(random.choices(string.ascii_letters + ' ', k=n))


# Function that generate random key pair
def generateKeyPair():
    keyB = random.randint(2, ALPHABET_LENGTH)
    keyA = 1
    for i in range(3, ALPHABET_LENGTH + 1):
        if gcd(i, keyB, ALPHABET_LENGTH) == 1: # Key should be co-primes
            keyA = i
            break
    return (keyA, keyB)


# Main tetsing function
def tester():
    print('Testing program has started')
    for i in range (3, 11, 2): # generate length
        print(f'Tests with length {i}:' )
        for _ in range(5): # 5 test per length

            # Generate key pair
            keyA, keyB = generateKeyPair()

            # Generate mock message
            message = generateRandomString(i)
            print(f'Message: {message} Keys: {keyA}, {keyB}')

            # Encrypt mock message
            encrypted = encryptMessage(message, keyA, keyB)
            print(f'Encrypted: {encrypted}')

            # Decrypt it again
            decrypted = decryptMessage(encrypted, keyA, keyB)

            # If they are equal then test has been passed
            print(f'''Result: {'PASS' if message == decrypted else 'FAIL'}''')

            # just a separator
            print('-' * 12 + '\n')


if __name__ == '__main__':
    tester()
