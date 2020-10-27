

text = input("Enter a 8-bit message to encrypt: ")
key = input("Enter a 10-bit key: ")
temp = ""

P10 = [3,5,2,7,4,10,1,9,8,6]
new_key = ""
for i in P10:
    new_key += key[i-1]

LK = new_key[0:5]
RK = new_key[5:10]

LK_1 = LK[1:5]+LK[0]
RK_1 = RK[1:5]+RK[0]

new_key = LK_1 + RK_1

K1 = ""
P8 = [6,3,7,4,8,5,10,9]
for i in P8:
    K1 += new_key[i-1]
print("p8 fo k1 is: ",K1)

LK_3 = LK_1[2:5]+LK_1[0:2]
RK_3 = RK_1[2:5]+RK_1[0:2]

new_key = LK_3 +RK_3

K2 = ""
for i in P8:
    K2 += new_key[i-1]
print("p8 fo k2 is: ",K2)

IP = [2,6,3,1,4,8,5,7]
for i in IP:
    temp += text[i-1]

LM = temp[0:4]
RM = temp[4:8]

new_RM = ""
EP = [4,1,2,3,2,3,4,1]
for i in EP:
    new_RM += RM[i-1]

temp = ""
for i in range (len(new_RM)):
    temp += str(int(new_RM[i])^int(K1[i]))

S0_i = int(temp[0]+temp[3],2)
S0_j = int(temp[1]+temp[2],2)
S1_i = int(temp[4]+temp[7],2)
S1_j = int(temp[5]+temp[6],2)

temp = ""
S0 = [['01','00','11','10'],['11','10','01','00'],['00','10','01','11'],['11','01','00','10']]
S1 = [['00','01','10','11'],['10','00','01','11'],['11','10','01','00'],['10','01','00','11']]
new_temp = S0[S0_i][S0_j]+S1[S1_i][S1_j]
P4 = [2,4,3,1]
for i in P4:
    temp += new_temp[i-1]

new_LM = ""

temp = S0[S0_i][S0_j]+S1[S1_i][S1_j]
for i in range(len(LM)):
    new_LM += str(int(temp[i])^int(LM[i]))

new_LM_2 = ""
for i in EP:
    new_LM_2 += new_LM[i-1]

temp = ""
for i in range (len(new_LM_2)):
    temp += str(int(new_LM_2[i])^int(K2[i]))

S0_i = int(temp[0]+temp[3],2)
S0_j = int(temp[1]+temp[2],2)
S1_i = int(temp[4]+temp[7],2)
S1_j = int(temp[5]+temp[6],2)

temp = ""
new_temp = S0[S0_i][S0_j]+S1[S1_i][S1_j]

for i in P4:
    temp += new_temp[i-1]

new_LM_3 = ""
temp = S0[S0_i][S0_j]+S1[S1_i][S1_j]
for i in range(len(RM)):
    new_LM_3 += str(int(temp[i])^int(RM[i]))

temp = ""
new_temp = new_LM_3 + new_LM
IPI = [4,1,3,5,7,2,8,6]

for i in IPI:
    temp += new_temp[i-1]

print("the cliphertext is: ",temp)
ciphertext = temp

temp = ""
for i in IP:
    temp += ciphertext[i-1]

LM = temp[0:4]
RM = temp[4:8]

new_RM = ""
for i in EP:
    new_RM += RM[i-1]

temp = ""
for i in range (len(new_RM)):
    temp += str(int(new_RM[i])^int(K2[i]))


S0_i = int(temp[0]+temp[3],2)
S0_j = int(temp[1]+temp[2],2)
S1_i = int(temp[4]+temp[7],2)
S1_j = int(temp[5]+temp[6],2)

temp = ""
new_temp = S0[S0_i][S0_j]+S1[S1_i][S1_j]

for i in P4:
    temp += new_temp[i-1]

new_LM = ""
for i in range(len(LM)):
    new_LM += str(int(temp[i])^int(LM[i]))

new_LM_2 = ""
for i in EP:
    new_LM_2 += new_LM[i-1]

temp = ""
for i in range (len(new_LM_2)):
    temp += str(int(new_LM_2[i])^int(K1[i]))

print("the key used in encryption: key1: "+new_RM+" , key2: %s: ",new_LM_2)

S0_i = int(temp[0]+temp[3],2)
S0_j = int(temp[1]+temp[2],2)
S1_i = int(temp[4]+temp[7],2)
S1_j = int(temp[5]+temp[6],2)

temp = ""
new_temp = S0[S0_i][S0_j]+S1[S1_i][S1_j]

for i in P4:
    temp += new_temp[i-1]

new_LM_3 = ""
for i in range(len(RM)):
    new_LM_3 += str(int(temp[i])^int(RM[i]))

temp = ""
new_temp = new_LM_3 + new_LM
for i in IPI:
    temp += new_temp[i-1]

print("the message is: ",temp)
print("\n171603010125蒙国安")