n = eval(input())
l = []
a = []
def f(n):
    if n == 1:
        return [['(',')']]
    elif n == 2:
        return [['(',')','(',')'],['(','(',')',')']]
    else:
        for i in f(n - 2):
            
