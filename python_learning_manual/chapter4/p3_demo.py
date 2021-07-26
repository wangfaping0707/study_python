L = [123, 'spam', 1.23]
print('列表L的长度：', len(L))


print(L[0])

# print(L[3])

print(L[-1])
# 列表的切片操作，不包括-1这个元素
print(L[:-1])


print(L + [4, 5, 6, 7])
print(L)

L.append('郑秋兰')
print('打印添加元素后的列表：', L)

# 在某个位置插入元素
L.insert(1, '北风吹')
print(L)
# 移除列表中的某个元素
L.remove(1.23)
print('移除元素1.23之后列表的打印：', L)

# 在列表尾部添加多个元素
L.extend(['love', 'the', 'world'])
print(L)



lis = [5,2,53,5,89,4,0,24,25]
lis.sort()
print('排序之后的列表：', lis)
lis.reverse()
print('反转之后的列表：', lis)














