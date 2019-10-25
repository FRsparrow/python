def getMaxLen(s):
    if len(s) == 1:
        return 1
    maxLen = 1
    tempMax = 1
    start = 0
    end = 1
    d = {}
    d[s[start]] = start
    while end < len(s):
        if s[end] in d:
            tempMax = end - d[s[end]]
            for i in s[start: d[s[end]]]:
                del d[i]
            start = d[s[end]] + 1
            d[s[end]] = end
            end += 1
            continue
        tempMax += 1
        if tempMax > maxLen:
            maxLen = tempMax
        d[s[end]] = end
        end += 1
    return maxLen

while True:
    s = input()
    print(getMaxLen(s))
