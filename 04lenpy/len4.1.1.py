
#列表,切片
lst1 = [1,2,3,4,5,6]
print(lst1[2:-2])
# 混合列表
lst2 = [lst1,11,12]
print(lst2, type(lst2), len(lst2))
# 添加元素
lst2.append(13)
print(lst2)
# 合并列表
lst3 = lst1 + lst2
print(lst3)
# 元素排序 sort() reverse()
lst3.reverse()
print(lst3)
print("-"*15)

# 元素合并
lst1.extend(lst2)
print(lst1)

# 元组。是只读列表
int1 = (1)
tup1 = (1,)
tup2= (1,2,3,4,5)
print(type(int1))
print(type(tup1))
print(tup2[:2])

# --------
print("-"*30)
list1 = [11,12,13]
list2 = [21,22,23]
list1.extend(list2)
print(list1)

list2.append(24)
list2.reverse()
print(list1)