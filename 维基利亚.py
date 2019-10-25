import math
import gmpy2

def get_key_length(cipher):
    keyLength= 1
    maxcount=0
    for i in range(2,13):
        count=0
        for j in range(i,len(cipher)-i):
            if  ord(cipher[j])-97==ord(cipher[j+i])-97:
                count+=1
            elif ord(cipher[j])-65 ==ord(cipher [j+i])-65:
                count+=1
            elif ord(cipher[j])-65 == ord(cipher[j+i])-97:
                count+=1
            elif ord(cipher[j])-97==ord(cipher[j+i])-65:
                count+=1
        if  count>maxcount:
            maxcount=count
            keyLength=i
    return keyLength
def count_list(ttt):
    ls = []
    for i in range(0,26):
        count=0
        for j in ttt:
            if  ord(j)-97==i:
                count+=1
            elif ord(j)-65 == i:
                count+=1
        ls.append(count/len(ttt))
    return ls

def guess_key(cipher,keylength):
    alphaRate =[0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008,0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001 ]
    key = []#保存秘钥
    #用keylength对密文分组，
    matrix = divide(cipher,keylength)
    #然后每一组凯撒密码计算重合指数
    for i in range(0,keylength):
        w = [row[i]  for  row in matrix] #这是我要判断的那一个组了
        ls = count_list(w)
        IC =[]  #记录26个不同秘钥时对应的重合指数
        for k in range(0,26):                      
            sum = 0.0
            for m in range(0,26):
                sum+=alphaRate[m]*ls[m]
            IC.append(sum)
            ls = ls[1:]+ls[:1]
            
        num =100
        sign = -1
        for i in range(0,26):
            if  abs(IC[i]-0.065546)<num:
                num =abs(IC[i]-0.065546)
                sign = i
        key.append(sign)
        
    return key      

def divide(cipher,keylength):
    matrix = []
    row=[]
    index =0
    for ch in cipher:
        row.append(ch)
        index+=1
        if  index %keylength==0:
            matrix.append(row)
            row=[ ]
    return matrix

aaa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher_temp=[]
cipher_temp= input("请输入待破解密文：")
cipher = []
origin = []
for  ch in range(0,len(cipher_temp)):
    if  cipher_temp[ch] in aaa:
        cipher.append(cipher_temp[ch])

print(get_key_length(cipher))

for i in range(2,13):
    key = []
    keylength = i
    key =guess_key(cipher,i)
    count = 0
    for  ch in cipher_temp:
        if   ord('a')<=ord(ch)<=ord('z'):
            origin.append(    chr(       (ord(ch)-ord('a')-key[count])    %26 + ord('a')     ))
            count+=1
            count %= keylength
        elif  ord('A')<=ord(ch)<=ord('Z'):
            origin.append(   chr(       (ord(ch)-ord('A')-key[count])    %26 + ord('A')     ))
            count+=1
            count %= keylength
        else :
            origin.append(ch)
        

    text=""
    for ch in origin:
        text+=ch
    print(key)
    print(text)
    origin = []
    print("\n\n")