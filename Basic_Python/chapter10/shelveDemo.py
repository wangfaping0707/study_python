import shelve
s = shelve.open('file.dat')
print(type(s))
s['x'] = ['a','b','c']
s['x'].append('d')
print(s['x'])