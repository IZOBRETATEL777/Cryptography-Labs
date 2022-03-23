#!/bin/python3

# Import for csv processing
import csv

# Import for working with paths
from os import path

# Imports for encryption/decryption
from decrypt import decryptMessage
from encrypt import encryptMessage

# Imports for cheking keys
from math import gcd

# Import for testing
from automated_testing import tester, ALPHABET_LENGTH

# Filepath constats
DB_FILENAME = 'studnet_database.csv'
MESSAGE_FILENAME = 'message.txt'


# function that add a student to csv file (aka our database)
def add_studnet():

    # Read all a data
    print('Enter next info:')

    idNumber = input('Enter ID#: ')
    name = input('Enter name: ')
    surname = input('Enter surname: ')

    subjects = []
    grades = []
    results = []

    n = None

    # asking user to enter info in proper way
    while n == None:
        try:
            n = int(input('Enter the number of subjects (at least five): '))
        except Exception:
            print('Wrong number')
        if n != None and n < 5:
            print('Try again')
            n = None
    for _ in range(n):
        subject = input('Enter Subject name: ')
        grade = None
        while grade == None:
            try:
                grade = int(input('Enter the score for subject. It should in from 0 to 100: '))
            except Exception:
                print('Wrong number')
            if grade != None and not 0 <= grade <= 100:
                print('Wrong range')
                grade = None
        subjects.append(subject)
        grades.append(grade)
        res = 'PASS' if grade >= 61 else 'FAIL'
        print('Subject result:', res)
        results.append(res)

    # If there is no database csv file program should create it
    if not path.exists(DB_FILENAME):
        print(f'Cannot find {DB_FILENAME}. It will be created.')
        with open(DB_FILENAME, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'NAME', 'SURNAME', 'SUBJECTS', 'GRADES', 'RESULT'])

    # Write all obtained data to csv
    with open(DB_FILENAME, 'a') as f:
        writer = csv.writer(f)

        # For data such as subjetcs or grades csv-arrays are used (just text separated with pipes |)
        row = [idNumber, name, surname, '|'.join(subjects), '|'.join([str(i) for  i in grades]), '|'.join(results)]
        writer.writerow(row)


# Get message from file our standard IO
def getMessage():
    msg = ''
    try:
        with open(MESSAGE_FILENAME) as f:
            msg = '\n'.join(f.readlines()) # join all lines of text to one string
    except Exception:
        print(f'Cannot access file {MESSAGE_FILENAME}. It will be created.')
    # Ask user to type message if our file is empty
    if not msg or msg.isspace():
        print('Please, enter message')
        msg = input()
    print('Message:', msg)
    return msg


# Function that gets key, pair from user
def getKeyPair():
    keyA = None
    keyB = None

    # Check if they are valid for Affine Cipher. GCD of them should be 1
    while keyA == None or keyB == None:
        try:
            print('Enter two keys in one line, they are should be co-prime with each other and 128:')
            keyA, keyB = map(int, input().split())
            if gcd(keyA, keyB, ALPHABET_LENGTH) != 1:
                raise Exception
        except Exception:
            print('Wrong! Try again!')
    return keyA, keyB


# Function that saves message to txt file
def saveMessage(message):
    # Write in safe manner
    try:
        with open(MESSAGE_FILENAME, 'w') as f:
            f.write(message)
    except Exception:
        print('Cannot write to the file')


# Driver code
def main():
    # Main menu
    while True:
        print('1. Enter student info:')
        print('2. Encryption')
        print('3. Decryption')
        print('4. Test')
        print('5. Exit')
        cmd = input('Enter command to continue: ')
        if cmd == '1':
            add_studnet()
        elif cmd == '2':
            msg = getMessage()
            keyA, keyB = getKeyPair()
            enc = encryptMessage(msg, keyA, keyB)
            print('Encrypted:', enc)
            saveMessage(enc)
        elif cmd == '3':
            msg = getMessage()
            keyA, keyB = getKeyPair()
            dec = decryptMessage(msg, keyA, keyB)
            print('Decrypted:', dec)
            saveMessage(dec)
        elif cmd == '4':
            tester()
        elif cmd == '5':
            print('Bye!')
            break
        else:
            print('Unknown command')

if (__name__ == "__main__"):
    main()

