def digit_number(n):
    i = 0
    while n // pow(10,i) != 0:
        i += 1
    return i
def digit(n):
    i = 1
    s = set()
    while i <= digit_number(n):
        s.add(n % 10)
        n //= 10
    return s
def half_factors(n):
    l = []
    for i in range(1,int(pow(n,0.5)) + 1):
        if n % i == 0:
          l.append(i)
    return l
s0= {0,1,2,3,4,5,6,7,8,9}
result = []
for i in range(1,100000000):
    l = half_factors(i)
    for j in l:
        if digit_number(i // j) + digit_number(i) + digit_number(j) == 10 and digit(i // j) | digit(i) | digit(j) == s0:
            result.append(i)
            result.append(j)
            result.append(i // j)
for i in result:
    print(i)
