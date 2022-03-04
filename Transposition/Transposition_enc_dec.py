#import necessary libs
from math import ceil

#define null character since space or \0 can be used in message
NULL_CHAR = '\0\0'

#funcion that prints table
def printTable(table: list, key: int):

    #define borders
    br = '-' * (key * 3) + '-'
    print(br)
    print('', end='|')
    #print header
    for i in range(1, key + 1):
        print(f'{i:2d}', end='|')
    print()
    print(br)
    #print data
    for row in table:
        print('', end='|')
        for ch in row:
            if ch == NULL_CHAR:
                ch = '•'
            print(' ' + ch, end='|')
        print()
        print(br)

#Recursive ecryprtion funcion
def encrypt(msg: str, key: int, table=[[]], cur=0):
    exit = False
    for _ in range(key):
        if cur == len(msg):
            #rise flag if no text left
            exit = True
            table[-1].append(NULL_CHAR)
        else:
            table[-1].append(msg[cur])
            cur += 1
    if not exit:
        #if no flag run recursive funcion again
        table.append([])
        return encrypt(msg, key, table, cur)
    else:
        # if flag print table and ecnrypt messsage
        printTable(table, key)
        enc = ''
        for j in range(key):
            enc += ''.join([row[j] for row in table if row[j] != NULL_CHAR])
        return enc

#Recursive decryption function
def decrypt(enc: str, key: int, table=[[]], columnNumber=0, sbCnt = 0, curRow=0):
    if columnNumber == 0:
        columnNumber = int(ceil(len(enc) / key))
        table = [[NULL_CHAR for _ in range(key)] for __ in range(columnNumber)]
        sbCnt = key * columnNumber - len(enc)
    # get row of the enctyption table with regards to space
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
        printTable(table, key)
        msg = ''
        for row in table:
            msg += ''.join([ch for ch in row if ch != NULL_CHAR])
        return msg
    else:
        return decrypt(enc, key, table, columnNumber, sbCnt, curRow + 1)


# Driver code
cmd = input('Enter 1 to encrypt or 2 to decrypt\n')
if cmd == '1':
    msg = input('Enter message: ')
    # validate key
    key = input(f'Enter key (2 to {len(msg) // 2}): ')
    if not key.isnumeric() or not 2 <= int(key) <= len(msg) // 2:
        print('Key is unacceptable')
        exit()
    key = int(key)
    enc = encrypt(msg, key)
    print("Encrypted:", enc)
elif cmd == '2':
    enc = input('Enter message: ')
    #validate key
    key = input(f'Enter key (2 to {len(enc) // 2}): ')
    if not key.isnumeric() or not 2 <= int(key) <= len(enc) // 2:
        print('Key is unacceptable')
        exit()
    key = int(key)
    msg = decrypt(enc, key)
    print("Decrypted:", msg)
else:
    print('No available option')

