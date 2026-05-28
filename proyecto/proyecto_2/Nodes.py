class Node:
    pass

class BinaryNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.left}, {self.right})"
        
class AssignNode(BinaryNode):
    def __repr__(self):
        return f"AssignNode({self.left}, {self.right})"
        
class IdentifierNode(Node):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"IdentifierNode({self.name})"
    
class IntNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"IntNode({self.value})"
        
class PowAssignNode(BinaryNode): pass
class IntDivAssignNode(BinaryNode): pass
class AssignNode(BinaryNode): pass