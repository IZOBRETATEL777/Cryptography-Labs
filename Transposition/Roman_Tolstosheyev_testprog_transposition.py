# import functions to be tested
from Roman_Tolstosheyev_transposition import encrypt, decrypt

# parse text file that was created after bruteforce
def parseTxt(filename:str) ->dict:
    tries = {}
    with open(filename, 'r') as f:
        for line in f:
            key = int(line.split()[1])
            message = line.split('"')[1]
            tries[key] = message
    return tries


if __name__ == '__main__':
    encrypted = parseTxt('bruteforced.txt')
    # get the order number, key and values from parsed data
    for idx, (key, plaintext) in enumerate(encrypted.items()):
        # encrypt text from parsed txt file and then decrypt again (like f^-1(f()))
        decrypted = decrypt(encrypt(plaintext, key), key)
        # if message in text and decrypted again message is the same test is passed. Otherwise, failed
        print(f'Testcase {idx + 1}: {"PASS" if plaintext == decrypted else "FAIL"}')

