import random

num = int(input("how many dice?"))
sides = int(input("how many sides per die?"))
sum = 0
for i in range(num):
    sum += random.randrange(1, sides + 1)

print("The result is ", sum)
