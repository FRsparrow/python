n = eval(input())
def kh(n):
    if n == 1:
        return ['()']
    else:
        for i in kh(n - 1):
            l = list(i)
            for j in l:
                if j == '(':
                    j = '(('
