s = input()
for i in range(1,26):
    temp = ''
    for j in s:
        if j.islower():
            temp += chr((ord(j)-ord('a')+i)%26 + ord('a'))
        elif j.isupper():
            temp += chr((ord(j)-ord('A')+i)%26 + ord('A'))
        else:
            temp += j
    print(temp)
