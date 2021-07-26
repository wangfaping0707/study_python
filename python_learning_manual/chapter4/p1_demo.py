S = 'shrubbery'
print('变化之前打印S:', S)

L = list(S)

print('将S序列化为列表:', L)

L[1] = 'C'

print('改变S序列化后:', L)

print('\\'.join(L))

print('验证S是否最终被改变：', S)

print(str(L))

ls = range(15, 30, 3)
print(type(ls))
for i in ls:
    print(i, end='  ')