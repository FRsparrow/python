card = []
result = [1]*54


for i in range(1,14):
    card.append('S' + str(i))
for i in range(1,14):
    card.append('H' + str(i))
for i in range(1,14):
    card.append('C' + str(i))
for i in range(1,14):
    card.append('D' + str(i))
card.append('J1')
card.append('J2')


n = eval(input())
so = input().split()
final = [result] * (n+1)
final[0] = card


for k in range(n):
    for i in range(54):
        final[k+1][int(so[i]) - 1] = final[k][i]


print(final[0])
print(final[1])
