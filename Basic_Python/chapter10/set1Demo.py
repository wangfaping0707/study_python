a = {1,2,3}
b = {2,3,4}
print(a.union(b))
print(a|b)

# 求得是交集
c = a & b
print("打印c的值", c)

# issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
print(c.issubset(b))

# issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
print(c.issuperset(a))
print(a.issuperset(c))

# intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。
print(a.intersection(b))


f = a.copy()
print(f)
print(f is a)

a1 = {2,0,3}
print(type(a1))
print(a1)
b1 =a1.copy()

print("a1的内存地址",id(a1))
print("b1的内存地址",id(b1))

