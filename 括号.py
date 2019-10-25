import random
n = eval(input())
sum = 0
a = []
result = []
while len(a) < pow(2,n * 2):
    b = []
    for i in range(n * 2):
        b.append(random.randrange(-1,2,2))
    if b not in a:
        a.append(b)
for p in a:
    for q in p:
        sum += q
        if sum < 0:
            break
    if sum == 0:
        result.append(p)
    sum = 0
for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] == 1:
            result[i][j] = '('
        else:
            result[i][j] = ')'
final = []
for i in result:
    final.append("".join(i))
print(final)
