def enCode():
    plainText = input('Enter a PlainText: ')
    keys = input('Enter a key: ')

    k = 0
    ciphertext = 'Ciphertext: '
    for i in range(len(plainText)):
        c = (ord(plainText[i]) - 97 + ord(keys[k]) - 97) % 26
        k = k + 1 if k + 1 < len(keys) else 0
        ciphertext+=chr(c + 97)

    print(ciphertext)



def deCode():
    ciphertext = input('Enter a ciphertext: ')
    keys = input('Enter a key: ')

    k = 0
    plaintext = 'Paintext: '
    for i in range(len(ciphertext)):
        c = (ord(ciphertext[i]) - 97 - ord(keys[k]) + 97) % 26
        k = k + 1 if k + 1 < len(keys) else 0
        plaintext+=chr(c + 97)

    print(plaintext)




print('VigenerePassword\n')

mode = input('select: e or d  : ')

if mode =='e':
    enCode()
elif mode=='d':
    deCode()