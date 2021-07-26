from collections.abc import Iterable,Iterator

d = {'a': 1, 'b': 2, 'c': 3}

print(d)

print(d.keys())

print(list(d.keys()))

d1 = {'lilee': 25, 'wangyan': 21, 'lidaming': 19}
print(d1.keys())
print(sorted(d1.keys()))
print(d1)

print('-----------------------------------------------分割线-----------------------------')
print(d1.items())
print(type(d1.items()))
print(d1)

print('d1.items()是可迭代对象吗？',isinstance(d1.items(),Iterable))
print("d1.items()是迭代器吗？",isinstance(d1.items(),Iterator))

# 对字典按照value值进行排序
print(sorted(d1.items(),key= lambda item:item[1]))








