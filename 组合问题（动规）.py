def f(n,s,l):
    if n == 0:
        if s == 0:
            return 1
        return 0
    return f(n-1,s,l)+f(i-1,s-l[n],l)
while True:
    try:
        n, s = map(int, input().split())
        l = list(map(int, input().split()))
        print(l)#print(f(n,s,l))
    except:
        break
    pass
