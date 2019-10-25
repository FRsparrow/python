def num(m, n):
    e = 0
    c = m
    if m % 2:
        c += 1
    for i in range(c,n+1,2):
        j = i
        while(j % 2 == 0):
            e += 1
            j = j >> 1
    return e
k = eval(input())
l = []
for i in range(k):
    str = input()
    m = int(str.split()[0])
    n = int(str.split()[1])
    a = num(n+1, m)
    b = num(2, m-n)
    l.append(a-b)
for i in l:
    print(i)
