# Clase con métodos dunder de un objeto iterable

class MyList:
    def __init__(self, items = [1, 2, 3]):
        self.items = items

    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index: int):
        return self.items[index % len(self.items)]
    
    def __setitem__(self, index: int, item):
        self.items[index % len(self.items)] = item
    
    def __contains__(self, item):
        return item in self.items
    
    def __len__(self):
        return len(self.items)

list1 = MyList([2, 3, 5, 7, 11, 13, 17])

for x in list1:
    print(x)


print(f"Item 4: {list1[3]}")
list1[3] = 1
print(f"New Item 4: {list1[3]}")
print(5 in list1)
print(len(list1))