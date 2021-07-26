# 列表推导表达式

L1 = [x for x in range(0, 5)]
print(L1)
L2 = [x + 1 for x in range(0, 5)]
print(L2)


print('------------------------------------------------------------')
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = [row[1] for row in M]
print(m1)


m2 = [row[1] + 1 for row in M]
print(m2)

# print([2,5,6] + 1)

m3 = [row[1] for row in M if row[1] % 2 == 0]
print(m3)

diag = [M[i][i] for i in range(0, 3)]
print(diag)


doubles = [c*2 for c in 'spam']
print(doubles)

print("使用range函数来生成列表：", list(range(4)))

print(list(range(-6,7,2)))


print([[x**2,x**3] for x in  range(4)])


print([[x, x // 2, x*2] for x in range(-6,7,2) if x > 0])

# G是一个生产器
G = (sum(row) for row in  M)
print(type(G))
for i in range(3):
    print(next(G),end='   ')
print("__________________________________________")
print(sum([1, 10, 20]))
