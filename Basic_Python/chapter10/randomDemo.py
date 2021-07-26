import random as r
"""
# 1、andom.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
"""
num = r.random()
print("打印生成的随机数：", num)
print("---------------------------------------------------------------------------------------------------")


"""
2、random.uniform(a,b) 用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: b <= n <= a。如果 a <b， 则 a <= n <= b
"""
print("随机角度：", r.uniform(0, 360))
print("随机数：", r.uniform(70, 60))

print("---------------------------------------------------------------------------------------------------")

"""
3、random.randrange([start], stop[, step]) 从指定范围内，按指定基数递增的集合中 获取一个随机数
random.randrange(10, 30, 2)，结果相当于从[10, 12, 14, 16, ... 26, 28]序列中获取一个随机数
"""
print("获取范围内，step=1的随机数：",r.randrange(1,5,1))
print("获取范围内，step=3的随机数：",r.randrange(10,30,3))

print("---------------------------------------------------------------------------------------------------")

"""
4、random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence) 
参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
"""
print("从字符串中随机获取一个字符：",r.choice("学习Python"))
print("从列表中随机获取一个元素：",r.choice(["JGood", "is", "a", "handsome", "boy"]))
print("从元组中随机获取一个元素:",r.choice(("Tuple", "List", "Dict")))


print("---------------------------------------------------------------------------------------------------")
"""
5、random.shuffle()  这个函数的作用是将一个列表中的元素打乱。它的函数原型为：random.shuffle(x[, random])。
"""
p = ["Python", "is", "powerful", "simple", "and so on..."]
print("打乱之前的列表：",p)
r.shuffle(p)
print("打乱之后的列表：",p)
print("---------------------------------------------------------------------------------------------------")

"""
6、random.sample(sequence, k)  从指定序列中随机获取指定长度的片断并随机排列。注意：sample函数不会修改原有序列
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(r.sample(lst,5))
print("验证lst是否变化：", lst)

"""
7、random.randint()  这个函数的作用是用于生成指定范围中的整数，它的函数原型是random.randint(a,b)。它和random.uniform()函数不同的是它的a是下限，b是上限。  
"""
print(r.randint(10, 20))  # 输出 12
print(r.randint(10,10))
# print(r.randint(110,10))    #Error



















