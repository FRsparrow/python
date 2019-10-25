import time as t

ans = 0;
start = t.time()
for i in range(10000):
    ans += i
end = t.time()
end -= start
print("标准循环时间：" + str(end))

ans = 0;
start = t.time()
for i in xrange(10000):
    ans += i
end = t.time()
end -= start
print("xrange循环时间：" + str(end))
'''
ans = 0;
start = t.time()
ans += i**2 for i in range(1e4)
end -= start
print("列表推断式循环时间：" + end)

ans = 0;
start = t.time()

end = t.time()
end -= start
print("标准循环时间：" + end)
'''
