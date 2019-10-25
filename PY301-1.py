# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准



fi = open("论语.txt", "r")
fo = open("论语-原文.txt", "w")
for line in fi:
    if "【" in line:
        flag = False
    if "【原文】" in line:
        flag = True
        continue
    if flag == True:
        fo.write(line.lstrip())
fi.close()
fo.close()

