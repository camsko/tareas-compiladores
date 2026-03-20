# Clase con métodos con estado

class LimitedStorage:
    def __init__(self, item = None):
        self.item = item

    def last_item(self):
        print(f"Last Item: {self.item}")

s = LimitedStorage('Item 1')
s.last_item()
s.item = 'Item 2'
s.last_item()