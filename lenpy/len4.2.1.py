# 函数
# python 内置 68 个函数, 可以返回多参
ss = 10
def add1(a,b,c=2):
    #ss = 3 全局变量在局部是不可变量
    sss =  ss + 1 
    print(sss)
    return a,b,c,a+b+c

print(add1(2,3), type(add1(2,3)))
print(ss)