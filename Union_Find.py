def union(s, a, b):     #合并s中a所在的集合和b所在的集合
    sa = set()
    sb = set()
    for i in s:
        if(a in i):
            sa = i
        if(b in i):
            sb = i
        if(sa != set() and sb != set()):
            break
    un = sa | sb
    s.remove(sa)
    s.remove(sb)
    s.append(un)
    return s
str = input()
n = int(str.split()[0])
m = int(str.split()[1])
s = []
for i in range(n):
    s.append({i+1})
for i in range(m):
    str = input()
    a = int(str.split()[0])
    b = int(str.split()[1])
    s = union(s, a, b)
max = 0
for i in s:
    if(len(i) > max):
        max = len(i)
print(max)
