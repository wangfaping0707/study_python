D = {'food': 'spam', 'quantity': 4, 'color': 'pink'}
print('打印food键对应的索引值：', D['food'])
# 改变quantity键对应的值
D['quantity'] = 20
print('d打印改变之后的字典：', D)

# 创建字典方式一
s = {}
print(s)
s['name'] = 'Bob'
s['age'] = 40
s['job'] = 'dev'
print(s)

# 创建字典方式二
s1 = dict(name='Bob', age=40, job='dev')
print(s1)


# 创建字段方式三
s2 = dict(zip(['name', 'age', 'job'], ['Bob', 40, 'dev']))
print(s2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 40.5}


print(rec['name'])

print(rec['name']['last'])

print(rec['job'])

print(rec['job'][-1])


rec['job'].append('janitor')

print(rec)


value = rec.get('hobby', 'reading')

print(rec)











