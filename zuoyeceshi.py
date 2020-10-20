


def enCode():
    keyMatrix = [[0, 0], [0, 0]]

    keyMatrix[0][0] = int(input('Enter a key: '))
    keyMatrix[0][1] = int(input('Enter a key: '))
    keyMatrix[1][0] = int(input('Enter a key: '))
    keyMatrix[1][1] = int(input('Enter a key: '))
    msg = input('Enter plaintext:')
    if len(msg) % 2 != 0:
        print('error')
        return
    index = 0
    ma1 = [0, 0]
    res = ''
    while index < len(msg):
        m1 = ord(msg[index]) - 97
        m2 = ord(msg[index + 1]) - 97
        index += 2
        ma1[0] = (m1 * keyMatrix[0][0] + m2 * keyMatrix[1][0]) % 26
        ma1[1] = (m1 * keyMatrix[0][1] + m2 * keyMatrix[1][1]) % 26
        res+=chr(ma1[0]+97)
        res+=chr(ma1[1] + 97)
    print('Ciphertext: '+res)


def getkey(k):
    j=00
    i=00
    while (i%26)!=1:
        i=int(k)*j
        j+=1
    k=j-1
    return k

def deCode():

    keyMatrix = [[0, 0], [0, 0]]

    keyMatrix[1][1] = int(input('Enter a key: '))
    keyMatrix[0][1] = -int(input('Enter a key: '))
    keyMatrix[1][0] = -int(input('Enter a key: '))
    keyMatrix[0][0] = int(input('Enter a key: '))
    md = getkey(keyMatrix[0][0]*keyMatrix[1][1]-keyMatrix[0][1]*keyMatrix[1][0])
    keyMatrix[0][0] = md*keyMatrix[0][0]%26
    keyMatrix[0][1] = md * keyMatrix[0][1] % 26
    keyMatrix[1][0] = md * keyMatrix[1][0] % 26
    keyMatrix[1][1] = md * keyMatrix[1][1] % 26

    msg = input('Enter ciphertext:')
    if len(msg) % 2 != 0:
        print('error')
        return
    index = 0
    ma1 = [0, 0]
    res = ''
    while index < len(msg):
        m1 = ord(msg[index]) - 97
        m2 = ord(msg[index + 1]) - 97
        index += 2
        ma1[0] = (m1 * keyMatrix[0][0] + m2 * keyMatrix[1][0]) % 26
        ma1[1] = (m1 * keyMatrix[0][1] + m2 * keyMatrix[1][1]) % 26
        res += chr(ma1[0] + 97)
        res += chr(ma1[1] + 97)
    print('Plaintext: ' + res)


print('HillPassWrod\n')

mode = input('select: e or d  : ')

if mode =='e':
    enCode()
elif mode=='d':
    deCode()
