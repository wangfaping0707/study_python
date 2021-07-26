
from heapq import *
from random import shuffle
"""
Python shuffle() 函数: shuffle() 方法将序列的所有元素随机排序。
注意：shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
random.shuffle (lst )         lst -- 可以是一个列表。
返回值:该函数没有返回值
"""
data = list(range(10))
shuffle(data)
print("查看打乱排序后的列表：", data)
heap = []
for n in data:
    heappush(heap, n)

print("加入元素后的heap：", heap)

heappush(heap, 1.66)
print(heap)

# heappop() 从堆中弹出最小的元素
a = heappop(heap)
print(a)
print("弹出元素后的堆：", heap)
# 函数heaprepace(heap,x) :从堆中弹出最小的元素，在压入一个新的元素，相比较于依次执行函数heappop和heappush，这个函数的效率更高
heapreplace(heap, 0.312)
print("执行heaprepace函数之后的变化：", heap)
