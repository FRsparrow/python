def isPrime(n):     #n > 2
    if(n == 1):
        return False
    if(n == 2 or n == 3):
        return True
    if(n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if(n % i == 0 or n % (i+4) == 0):
            return False
        i += 6
    return True
n = eval(input())
l = []
for i in range(n):
    k = eval(input())
    len = 1
    if(isPrime(k)):
        l.append(0)
        continue
    elif(k % 2):
        i = 2
        while(not isPrime(k-i)):
            len += 2
            i += 2
        len += 1
        i = 2
        while(not isPrime(k+i)):
            len += 2
            i += 2
        l.append(len+2)
    else:
        i = 1
        while(not isPrime(k-i)):
            len += 2
            i += 2
        i = 1
        while(not isPrime(k+i)):
            len += 2
            i += 2
        l.append(len+1)
for i in l:
    print(i)
        
            
