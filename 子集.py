import copy
def subset1(s):
    if s == set():
        return [s]
    x = max(s)
    l1 = subset1(s-{x})
    l2 = copy.deepcopy(l1)
    for i in l2:
        i.add(x)
    return l1+l2
s = {1,2,3,4,5}
print(subset1(s))
def subset2(s):
    if s == []:
        return [s]
    if len(s) == 1:
        return [[],s]
    mid = int(len(s) / 2)
    l1 = subset2(s[:mid])
    l2 = subset2(s[mid:])
    l = []
    for i in l1:
        for j in l2:
            l.append(i+j)
    return l
s1 = [1,2,3,4,5]
print(subset2(s1))
