# 字典,无序
map1 = {1:"你好","world":3}
print(map1)
print(map1[1], map1["world"])

for entity in map1.items():
    print(entity, type(entity))

# 添加字典
map1[11.1]="score"
for k,v in map1.items():
    print(type(k),type(v))
    print("map entity: %s=" %(k),v)

map2 = {"hai":1, "lll":2}

map1.update(map2)
print(map1)

map1.pop("lll")
print(map1)

# 集合 ，集合内数据是唯一的
set1 = {1,2,3,4,5}
print(set1, type(set1), len(set1))
set1.add(6)
print(set1, type(set1), len(set1))

set2 = set({1,2,3})
set2.add(4)
print(set2, type(set2), len(set2))

# 不变集合
set3 = frozenset({1,2,3})
print(set3, type(set3), len(set3))
