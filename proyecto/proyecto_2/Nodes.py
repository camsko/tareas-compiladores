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

class FunctionNode(Node):
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        return f"FunctionNode(name={self.name}, parameters={self.parameters}, body={self.body})"
    
class ParameterNode(Node):
    def __init__(self, name, default_value=None):
        self.name = name
        self.default_value = default_value

    def __repr__(self):
        return (
            f"ParameterNode("
            f"{self.name}, "
            f"{self.default_value})"
        )

class IfNode(Node):
    def __init__(self, conditions, body, elif_list=None, else_=None):
        self.conditions = conditions
        self.body = body
        self.elif_list = elif_list
        self.else_ = else_

    def __repr__(self):
        return f"IfNode(conditions={self.conditions}, body={self.body}, elif_list={self.elif_list}, else={self.else_})"
    
class ElifNode(Node):
    def __init__(self, conditions, body):
        self.conditions = conditions
        self.body = body

    def __repr__(self):
        return f"ElifNode(conditions={self.conditions}, body={self.body})"
    
class ElseNode(Node):
    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return f"ElseNode(bodys={self.body})"
        
class PowAssignNode(BinaryNode): pass
class IntDivAssignNode(BinaryNode): pass
class PlusAssignNode(BinaryNode): pass
class MinusAssignNode(BinaryNode): pass
class MultAssignNode(BinaryNode): pass
class DivAssignNode(BinaryNode): pass
class ModAssignNode(BinaryNode): pass
class AssignNode(BinaryNode): pass
class EqualNode(BinaryNode): pass
class NonEqualNode(BinaryNode): pass
class AndNode(BinaryNode): pass
class OrNode(BinaryNode): pass