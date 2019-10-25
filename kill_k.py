s = input()
k = eval(input())
l = []
#len(s) >= k
def get_head(s,k):
    length = len(s)
    min = 10
    idx = 0
    for i in range(length-k+1):
        if(int(s[i]) < min):
            min = int(s[i])
            idx = i
    l.append(s[idx])
    return idx
for i in range(k):
    idx = get_head(s,k-i)
    s = s[idx+1:]
result = ''
for i in l:
    result += i
print(result)
