#!/bin/python3

# Important constants
MESSAGE_FILENAME = 'message.txt'
ALPHABET_LENGTH = 128


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
    else:
        print('Message:', msg)
        cmd = ''
        # Ask user if he/she wants to enter new message
        while cmd == '':
            cmd = input('Do you want to enter another message? Y/N: ')
            if cmd == 'Y':
                print('Enter new message:')
                msg = input()
            elif cmd == 'N':
                break
            else:
                print('So Y or N?')
                cmd = ''
    return msg


# Function that saves message to txt file
def saveMessage(message):
    # Write in safe manner
    try:
        with open(MESSAGE_FILENAME, 'w') as f:
            f.write(message)
    except Exception:
        print('Cannot write to the file')


# Decryption function for character that also show what it did
def decryptMessage(chrTr, chrKey):
    chrTrAscii = ord(chrTr)
    chrKeyAscii = ord(chrKey)
    # Using formula for a character
    newCharAscii = (chrTrAscii - chrKeyAscii) % ALPHABET_LENGTH
    newChar = chr(newCharAscii)
    print(f'Character {chrTr} (ASCII {chrTrAscii}) => Character {newChar} (ASCII {newCharAscii}) via key {chrKey} (ASCII {chrKeyAscii})')
    return newChar


# Encryption function for character that also show what it did
def encryptMessage(chrTr, chrKey):
    chrTrAscii = ord(chrTr)
    chrKeyAscii = ord(chrKey)
    # Using formula for a character
    newCharAscii = (chrTrAscii + chrKeyAscii) % ALPHABET_LENGTH
    newChar = chr(newCharAscii)
    print(f'Character {chrTr} (ASCII {chrTrAscii}) => Character {newChar} (ASCII {newCharAscii}) via key {chrKey} (ASCII {chrKeyAscii})')
    return newChar



# Recursive function that translate each character depending on intent (encryption or decryption)
def translate(message, key, intent, curMessageIdx=0, curTranslated='', curKeyIdx=0):
    if curKeyIdx == len(key): # if indexes of key are finished then start with 0 again
        return translate(message, key, intent, curMessageIdx, curTranslated, curKeyIdx=0)
    elif curMessageIdx == len(message): # if indexes of message are finished then return encrypted message
        return curTranslated
    else: # otherwise continue to process message
        curTranslated += intent(message[curMessageIdx], key[curKeyIdx])
        return translate(message, key, intent, curMessageIdx+1, curTranslated, curKeyIdx+1)


# Driver code
def main():
    # Main menu
    while True:
        print('1. Encryption')
        print('2. Decryption')
        print('3. Exit')
        cmd = input('Enter command to continue: ')
        if cmd == '1':
            msg = getMessage()
            key = input('Enter key: ')
            # Send encryption intent
            enc = translate(msg, key, encryptMessage)
            print('Encrypted:', enc)
            saveMessage(enc)
        elif cmd == '2':
            msg = getMessage()
            key = input('Enter key: ')
            # Send decryption intent
            dec = translate(msg, key, decryptMessage)
            print('Decrypted:', dec)
            saveMessage(dec)
        elif cmd == '3':
            print('Bye!')
            break
        else:
            print('Unknown command')

if (__name__ == "__main__"):
    main()

