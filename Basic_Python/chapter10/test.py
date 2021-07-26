
import copy

print("模块copy的属性：",dir(copy))


list = [n for n in dir(copy) if not n.startswith('_')]
print(list)


print(copy.__all__)

print(help(copy.copy))

print("------------------------------------------------------------")

print(copy.copy.__doc__)

print("************************************************")
print(help(help()))


