class MyDict(dict):
    def get(self, key, default_val=0):
        return super().get(key, default_val)

    def __getitem__(self, item):
        if hasattr(MyDict, str(item)) is False:
            return 0

    def __add__(self, other):
        if isinstance(other, list):
            for i in other:
                if i not in self.keys():
                    self[i] = 0
        return self
    def __sub__(self, other):
        if isinstance(other, list):
            for i in other:
                if i in self.keys():
                    self.pop(i)
        return self



a = MyDict({1: 1, 2: 2})
#print(a[3])

r = [2, 3, 4, 5]
print(a - r)