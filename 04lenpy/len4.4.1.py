# 文件读写
import os

print(os.getcwd())

# 默认只读打开
file1 = open("file.txt")
print(file1.read())
file1.close()
print("-"*20)

# 追写打开
file2 = open("file.txt", 'a')
file2.write("\nwelcome")
file2.close()

# 按行读取
file3 = open("file.txt")
line = file3.readline()
while line:
    print(line)
    line = file3.readline()
file3.close()
print("-"*20)

# 覆盖写打开，如果没有文件会创建一个新文件
file4 = open("file.txt", 'w')
file4.write("welcome")
file4.close()

file5 = open("file.txt")
print(file5.read())
file5.close()
print("-"*20)

import this
