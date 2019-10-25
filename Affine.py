s = input()
txt = "abcdefghijklmnopqrstuvwxyz .,"
map = {}
for i in range(29):
    map[txt[i]] = i
for a in range(1,29):
    for b in range(29):
        temp = ''
        for i in s:
            if i in txt:
                temp += txt[(a * map[i] + b) % 29]
            else:
                temp += i
        if 'the' in temp:
            print(temp)
