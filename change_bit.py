s = input()
length = len(s)
print(length)
for row in range(2,13):
    if length % row == 0:
        temp = ""
        col = int(length / row)
        for i in range(col):
            for j in range(i, length, col):
                temp += s[j]
        print(temp)
