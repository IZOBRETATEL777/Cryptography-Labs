
# define necessary variables
message = '''"Hello Azerbaijan"'''
keyA = 0
keyB = 0

# The number of chars in ASCII table
alphabetLen = 128

# Input keys using validation
while True:
    keyA = int(input('Enter key A: '))
    if not 1 < keyA < alphabetLen:
        print('Invalid key')
        continue
    else:
        break

while True:
    keyB = int(input('Enter key B: '))
    if not 1 < keyA < alphabetLen:
        print('Invalid key')
        continue
    else:
        break


# Get ASCII codes of chars in message
codes = [ord(i) for i in message]

print('ASCII in messages')
print(*codes, sep=' ')

# Encrypt each character using (ax + b) mod n formula
for i in range(len(codes)):
    codes[i] *= keyA
    codes[i] += keyB
    codes[i] %= alphabetLen


print('Encoded ASCII in messages')
print(*codes, sep=' ')

# Convert codes to symbols
encrypted = ''.join([chr(i) for i in codes])

print('Warring! Not all character can be printable')
# Print message
print(encrypted)


