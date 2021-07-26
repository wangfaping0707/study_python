import sys, pprint


def printHello():
    print("hello,python")


# printHello()
if __name__ == '__main__':
    printHello()

pprint.pprint(sys.path)



print(dir('hello'))