
x,y=3,5
# ifelse分支控制
if x<y:
    print("x<y")
elif x>y:
    print("x>y")
else:
    print("x==y")

# 三目运算 等价 print(x>y?x:y)
print(x if x>y else y)
