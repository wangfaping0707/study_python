from collections.abc import Iterator,Iterable

class TestIterator():
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
print("ti是迭代器吗？", isinstance(ti, Iterator))
print(ti)
print(list(ti))