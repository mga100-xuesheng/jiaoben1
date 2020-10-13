import string

plaintext_ = string.ascii_lowercase  # string.ascii_letters
ciphertext_ = string.ascii_uppercase


# 加密算法

def encryption(K1, K2, plaintext):
    cipherarr = [0 for i in range(len(plaintext))]
    plaintext_list = list(plaintext)

    j = 0
    for plaintext_item in plaintext_list:
        for i in range(len(plaintext_)):
            if plaintext_item == plaintext_[i]:
                ciphertext = (int(K1) * i + int(K2)) % 26
                cipherarr[j] = ciphertext_[ciphertext]
                print(ciphertext, " ", cipherarr[j])
                j = j + 1
    cipher = ''.join(cipherarr)
    return cipher


while True:
    print('========加密部分========')
    K1 = input('请输入K1：')
    K2 = input('请输入K2：')
    plaintext = input('请输入消息：')
    print('对应密文是:')
    cipher = encryption(K1, K2, plaintext)
    # if plaintext == 'exit':
    #     break
    print('密文是:', cipher)
    break


# 解密算法

def decryption(K3, K4, ciphertext):
    plaintext_arr = [0 for i in range(len(ciphertext))]
    cipherlist = list(ciphertext)

    j = 0
    for cipheritem in cipherlist:
        for i in range(len(ciphertext_)):
            if cipheritem == ciphertext_[i]:
                plaintext = (key1(K3) * (i - int(K4))) % 26
                plaintext_arr[j] = plaintext_[plaintext]
                print(plaintext, " ", plaintext_arr[j])
                j = j + 1
    plain = ''.join(plaintext_arr)

    return plain


# 乘法可逆

def key1(K3):
    j = 00
    i = 00
    while (i % 26) != 1:
        i = int(K3) * j
        j += 1
    K3 = j - 1
    return K3


while True:
    print('\n=========解密部分========')
    K3 = input('请输入K3：')
    K4 = input('请输入K4：')
    ciphertext = input('请输入密文：')
    print('对应明文是:')
    plain = decryption(K3, K4, ciphertext)
    # if ciphertext == 'EXIT':
    #     break
    print('明文输出为：', plain)
    break
