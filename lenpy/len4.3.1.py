# 面向对象
from module.mymodule import Man, SupperMan

m = Man(1)
m.setAge(30)
m.name="lll"
print(m.getAge(), m.age, m.name, type(m))
print("-"*30)

m.printName()
m.setName("happy")
print(m.name)
m.printName()
del m

print("-"*30)
sman = SupperMan(2)
sman.printName()