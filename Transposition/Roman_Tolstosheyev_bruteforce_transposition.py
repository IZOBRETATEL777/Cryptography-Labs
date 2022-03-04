#import necessary libs
from math import ceil

#define null character since space or \0 can be used in message
NULL_CHAR = '\0\0'

#Recursive decryption function
def decrypt(enc: str, key: int, table=[[]], columnNumber=0, sbCnt = 0, curRow=0):
    if columnNumber == 0:
        columnNumber = int(ceil(len(enc) / key))
        table = [[NULL_CHAR for _ in range(key)] for __ in range(columnNumber)]
        sbCnt = key * columnNumber - len(enc)
    # get row of the encryption table with regards to space
    if key - sbCnt <= curRow:
        row = [_ for _ in enc[:columnNumber - 1]]
        #remove processed encrypted text
        enc = enc[columnNumber - 1:]
    else:
        row = [_ for _ in enc[:columnNumber]]
        enc = enc[columnNumber:]
    for i in range(columnNumber):
        if i < len(row):
            table[i][curRow] = row[i]
    # if no text left merging table into message
    if len(enc) == 0:
        msg = ''
        for row in table:
            msg += ''.join([ch for ch in row if ch != NULL_CHAR])
        return msg
    else:
        return decrypt(enc, key, table, columnNumber, sbCnt, curRow + 1)

# bruteforce function
def bruteforce(encryptedMesssage: str) -> dict:
    tries = {}
    for key in range(2, len(encryptedMesssage) // 2):
        res = decrypt(encryptedMesssage, key)
        tries[key] = res
    # return keys and decrypted with this key plaintext
    return tries


# Driver code
if __name__ == '__main__':
    encryptedMesssage = ''
    # trying to get message frome file
    try:
        with open('transposition_encryption.txt', 'r') as encryptedFile:
            encryptedMesssage = encryptedFile.readline()
            if encryptedMesssage[-1] == '\n':
                encryptedMesssage = encryptedMesssage[:-1]
    except IOError:
        print('Cannot access the file')
        exit()
    print(encryptedMesssage)
    # start bruteforce
    results = bruteforce(encryptedMesssage)
    # write keys and corresponding decrypted messages to file
    with open('bruteforced.txt', 'w') as f:
        for key, res in results.items():
            out = f'Key: {key} message: \"{res}\"'
            print(out)
            f.write(out + '\n')


