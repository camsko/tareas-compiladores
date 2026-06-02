class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"ProgramNode(\n{self.statements}\n)" 
    
    def __iter__(self):
        return iter(self.statements)

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

class MemberAccessNode(Node):
    def __init__(self, base, members):
        self.base = base
        self.members = members

    def __repr__(self):
        return f"MemberAccessNode(base={self.base}, members={self.members})"
    
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

class BoolNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"BoolNode({self.value})"

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
        
class FunctionCallNode(Node):
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def __repr__(self):
        return (
            f"FunctionCallNode("
            f"{self.name}, "
            f"{self.parameters})"
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
    
class TryNode(Node):
    def __init__(self, body, except_list):
        self.body = body
        self.except_list = except_list

    def __repr__(self):
        return f"TryNode(body={self.body}, except_list={self.except_list})"

class ExceptNode(Node):
    def __init__(self, exception, name, body):
        self.exception = exception
        self.name = name
        self.body = body

    def __repr__(self):
        return f"ExceptNode(exception={self.exception}, name={self.name}, body={self.body})"

class WhileNode(Node):
    def __init__(self, conditions, body):
        self.conditions = conditions
        self.body = body

    def __repr__(self):
        return f"WhileNode(conditions={self.conditions}, body={self.body})"
    
class ForNode(Node):
    def __init__(self, i_var, gen_func, body):
        self.i_var = i_var
        self.gen_func = gen_func
        self.body = body

    def __repr__(self):
        return f"ForNode(iterable variable={self.i_var}, generator function={self.gen_func}, body={self.body})"
    
class RangeNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"RangeNode({self.value})"
    
class IndexNode(Node):
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __repr__(self):
        return f"IndexNode({self.value}, {self.index})"
    
class MethodCallNode(Node):
    def __init__(self, obj, method, args):
        self.obj = obj
        self.method = method
        self.args = args

    def __repr__(self):
        return (
            f"MethodCallNode("
            f"obj={self.obj}, "
            f"method={self.method}, "
            f"args={self.args})"
        )
    
class ClassNode(Node):
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __repr__(self):
        return f"ClassNode(name={self.name}, body={self.body})"
    
class ChildClassNode(Node):
    def __init__(self, name, parent, body):
        self.name = name
        self.parent = parent
        self.body = body

    def __repr__(self):
        return f"ChildClassNode(name={self.name}, parent={self.parent}, body={self.body})"
    
class ClassBodyNode(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"ClassBodyNode(statements={self.statements})"

class ReturnNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ReturnNode({self.value})"
    
class ParameterHintNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ParameterHintNode({self.value})"

class ListNode(Node):
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"ListNode({self.elements})"
    
class TupleNode(Node):
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"TupleNode({self.elements})"
    
class DictNode(Node):
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"DictNode({self.elements})"

class BreakNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"BreakNode({self.value})"

class ContinueNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"ContinueNode({self.value})"
    
class PassNode(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PassNode({self.value})"
        
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
class LowerThanNode(BinaryNode): pass
class GreaterThanNode(BinaryNode): pass
class LowerEqualNode(BinaryNode): pass
class GreaterEqualNode(BinaryNode): pass
class AndNode(BinaryNode): pass
class OrNode(BinaryNode): pass
class RangeBinaryNode(BinaryNode): pass
class PlusNode(BinaryNode): pass
class MultNode(BinaryNode): pass
class NotNode(BinaryNode): pass
class PowNode(BinaryNode): pass
class IntDivNode(BinaryNode): pass
class MinusNode(BinaryNode): pass
class DivNode(BinaryNode): pass
class ModNode(BinaryNode): pass
