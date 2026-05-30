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
    
    
class StringNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"StringNode({self.value})"  
    
class FloatNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"FloatNode({self.value})"  

class IntNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"IntNode({self.value})"
        
class PowAssignNode(BinaryNode): pass
class IntDivAssignNode(BinaryNode): pass
class PlusAssignNode(BinaryNode): pass
class MinusAssignNode(BinaryNode): pass
class MultAssignNode(BinaryNode): pass
class DivAssignNode(BinaryNode): pass
class ModAssignNode(BinaryNode): pass
class AssignNode(BinaryNode): pass