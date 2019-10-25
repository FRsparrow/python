s = input()
n = eval(s)
l = []
for i in s:
    l.append(i)
d = 2 * n
sd = str(d)
for j in sd:
    if j in l:
        l.remove(j)
if l == []:
    print("Yes")
    print(d)
else:
    print("No")
