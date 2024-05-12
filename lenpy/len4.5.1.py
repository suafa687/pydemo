
# 异常
try:
    file1 = open("file1.txt")
except Exception as e:
    print(e)
finally:
    print("end")

with open("file.txt") as f:
    print(f.read())

print("-"*20)

from module.mymodule import SupperMan

with SupperMan() as supperMan:
    supperMan.printName()